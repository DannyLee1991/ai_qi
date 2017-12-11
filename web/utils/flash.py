from flask import flash

def flash_success(msg):
    flash(msg, "success")


def flash_info(msg):
    flash(msg, "info")


def flash_warning(msg):
    flash(msg, "warning")


def flash_danger(msg):
    flash(msg, "danger")
