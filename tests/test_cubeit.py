"""Smoke tests for the cubeit web page"""

from typing import Final

from playwright.sync_api import Page, expect


BASE_URL: Final = "http://localhost:8080"


def test_cube(page: Page):
    """Test the cube page funcitonality"""
    page.goto(url=BASE_URL)

    # Enter a value
    input_box = page.get_by_placeholder("enter number...")
    input_box.fill("13")

    # Click the "Cube" button
    page.get_by_role("button", name="Cube").click()

    # Get the result
    # Example: 133 = 2197
    result = page.locator("css=p#result")

    expect (result).to_contain_text("2197")


def test_cube_empty_imput(page: Page):
    """Test the cube page with empty input"""
    page.goto(url=BASE_URL)

    # Click the "Cube" button
    page.get_by_role("button", name="Cube").click()

    # Get the result
    result = page.locator("css=p#result")

    expect (result).to_contain_text("Enter something!")
