"""Pytest configuration for stress tests."""


def pytest_html_report_title(report):
    """Set the HTML report title."""
    report.title = "Stress Tests"
