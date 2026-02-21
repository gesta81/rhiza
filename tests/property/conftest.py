"""Pytest configuration for property-based tests."""


def pytest_html_report_title(report):
    """Set the HTML report title."""
    report.title = "Hypothesis Property Tests"
