#!/bin/bash
set -e

echo "==================================="
echo "PMS Test Automation Container"
echo "==================================="
echo ""

# Function to wait for Selenium Grid
wait_for_selenium() {
    echo "Waiting for Selenium Grid at $SELENIUM_HUB..."
    local timeout=60
    local start_time=$(date +%s)

    while true; do
        if curl -s "$SELENIUM_HUB/status" | grep -q '"ready":true'; then
            echo "✓ Selenium Grid is ready!"
            return 0
        fi

        local current_time=$(date +%s)
        local elapsed=$((current_time - start_time))

        if [ $elapsed -ge $timeout ]; then
            echo "✗ Timeout waiting for Selenium Grid after ${timeout}s"
            return 1
        fi

        echo "  Waiting... (${elapsed}s/${timeout}s)"
        sleep 2
    done
}

# Function to run tests
run_tests() {
    local marker="${1:-all}"
    local workers="${2:-4}"

    echo ""
    echo "Running tests..."
    echo "  Marker: $marker"
    echo "  Workers: $workers"
    echo "  Browser: ${BROWSER:-chrome}"
    echo ""

    if [ "$marker" = "all" ]; then
        pytest src/tests/ \
            -v \
            -n "$workers" \
            --alluredir=allure-results \
            --tb=short
    else
        pytest src/tests/ \
            -m "$marker" \
            -v \
            -n "$workers" \
            --alluredir=allure-results \
            --tb=short
    fi
}

# Main execution
case "$1" in
    --wait-for-selenium)
        wait_for_selenium
        ;;
    --test)
        shift
        wait_for_selenium
        run_tests "${1:-all}" "${2:-4}"
        ;;
    --smoke)
        wait_for_selenium
        run_tests "smoke" "2"
        ;;
    --regression)
        wait_for_selenium
        run_tests "regression" "4"
        ;;
    --help|*)
        cat << EOF
Usage: docker run <image> [COMMAND]

Commands:
  --wait-for-selenium    Wait for Selenium Grid to be ready
  --test [MARKER] [N]    Run tests with specified marker using N workers
  --smoke                Run smoke tests (2 workers)
  --regression           Run regression tests (4 workers)
  --help                 Show this help message

Environment Variables:
  SELENIUM_HUB          Selenium Grid URL (default: http://localhost:4444/wd/hub)
  BROWSER               Browser to use (default: chrome)
  ENV                   Test environment (default: demo)

Examples:
  # Run smoke tests
  docker run --env SELENIUM_HUB=http://selenium-hub:4444/wd/hub <image> --smoke

  # Run all tests with 4 workers
  docker run --env SELENIUM_HUB=http://selenium-hub:4444/wd/hub <image> --test all 4

  # Just wait for Selenium Grid
  docker run --env SELENIUM_HUB=http://selenium-hub:4444/wd/hub <image> --wait-for-selenium
EOF
        ;;
esac
