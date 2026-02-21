"""Pytest configuration for property-based tests."""

import os


def pytest_html_report_title(report):
    """Set the HTML report title from the PYTEST_HTML_TITLE environment variable."""
    title = os.environ.get("PYTEST_HTML_TITLE")
    if title:
        report.title = title
