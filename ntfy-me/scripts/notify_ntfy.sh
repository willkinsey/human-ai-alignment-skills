#!/bin/sh
set -eu

# Keep topic validation byte-oriented and make the allowed character ranges
# unambiguous across locales. The topic is a bearer-like secret, so never echo
# it or include it in an error message.
LC_ALL=C
export LC_ALL

KEYCHAIN_SERVICE=codex-ntfy-topic
NTFY_ENDPOINT=https://ntfy.sh
TITLE=
PRIORITY=default
TAGS=
MESSAGE=

usage() {
  cat >&2 <<'EOF'
Usage: notify_ntfy.sh --message TEXT [--title TEXT] [--priority LEVEL] [--tags TAGS]
  --message TEXT       Required notification body
  --title TEXT         Optional notification title
  --priority LEVEL     min, low, default, high, or max (default: default)
  --tags TAGS          Optional comma-separated ntfy tags
EOF
}

usage_error() {
  echo "Invalid ntfy notification arguments." >&2
  usage
  exit 2
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --message)
      [ "$#" -ge 2 ] || usage_error
      MESSAGE=$2
      shift 2
      ;;
    --title)
      [ "$#" -ge 2 ] || usage_error
      TITLE=$2
      shift 2
      ;;
    --priority)
      [ "$#" -ge 2 ] || usage_error
      PRIORITY=$2
      shift 2
      ;;
    --tags)
      [ "$#" -ge 2 ] || usage_error
      TAGS=$2
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      usage_error
      ;;
  esac
done

if [ -z "$MESSAGE" ]; then
  echo "Notification message is required." >&2
  exit 2
fi

case "$PRIORITY" in
  min|low|default|high|max) ;;
  *)
    echo "Invalid ntfy priority." >&2
    exit 2
    ;;
esac

# NTFY_TOPIC is intentionally an ephemeral test hook. In normal operation,
# the topic comes from the macOS Keychain item owned by the current account.
if [ "${NTFY_TOPIC+x}" = x ]; then
  TOPIC=$NTFY_TOPIC
else
  if [ -z "${USER:-}" ]; then
    echo "The current macOS user is unavailable for Keychain lookup." >&2
    exit 1
  fi

  if ! TOPIC=$(security find-generic-password \
    -a "$USER" \
    -s "$KEYCHAIN_SERVICE" \
    -w 2>/dev/null); then
    echo "ntfy topic is not configured in Keychain." >&2
    exit 1
  fi
fi

case "$TOPIC" in
  ""|*[!A-Za-z0-9_-]*)
    echo "ntfy topic is empty or contains unsupported characters." >&2
    exit 2
    ;;
esac

if [ "${#TOPIC}" -gt 64 ]; then
  echo "ntfy topic is longer than 64 characters." >&2
  exit 2
fi

# Read the body from stdin so curl treats a leading '@' as message text, not a
# filename. Suppress curl's response and diagnostics so secrets never appear
# in output; the caller receives a stable safe error instead.
if ! printf '%s' "$MESSAGE" | curl \
  --fail \
  --silent \
  --show-error \
  --max-time 15 \
  --request POST \
  --header "Title: $TITLE" \
  --header "Priority: $PRIORITY" \
  --header "Tags: $TAGS" \
  --data-binary '@-' \
  "$NTFY_ENDPOINT/$TOPIC" \
  >/dev/null 2>/dev/null; then
  echo "ntfy notification request failed." >&2
  exit 1
fi
