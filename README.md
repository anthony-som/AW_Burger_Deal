# A&W Teen Burger Deal Notification App

## Overview

The A&W Burger Deal Notification App is designed to notify you when there is a $2 Teen burger deal on the A&W App through a toast notification on Windows 10. 
<p align="center">
  <img src="https://github.com/anthony-som/AW-Burger-Deal/assets/98991855/b7e4560e-6116-47e2-811c-1ac13a14375d" width="50%" height="50%">
</p>

## How It Works

The A&W Burger Deal Notification App seamlessly integrates with your daily routine to ensure you never miss out on a special $2 Teen Burger offer whenever the Toronto Maple Leafs play. Here's a detailed breakdown of how the app functions:

1. **NHL Schedule Fetching**: The app communicates with the NHL's official API (https://api-web.nhle.com/) to retrieve the game schedule for the Toronto Maple Leafs. This operation is performed every 24 hours to ensure the app has the most up-to-date information.

2. **Date Comparison**: Utilizing the `datetime` library, the app compares the current date with the Maple Leafs' game schedule. This step is crucial for determining whether there's a game on any given day.

3. **Notification Alert**: If the app detects a match between today's date and a game day, it triggers a Windows notification. This alert serves as a friendly reminder that a $2 Teen Burger offer is available at A&W, tied to the Maple Leafs' game day.

By leveraging real-time data and timely notifications, the A&W Burger Deal Notification App ensures that you're always in the loop about the next opportunity to enjoy a discounted Teen Burger during Toronto Maple Leafs games.


## Error Resolution

If you receive the following error:

```bash
TypeError: WPARAM is simple, so must be an int object (got NoneType)
```

This indicates an issue with the handling of notification events. To resolve this, you need to update a function in the win10toast library, which is responsible for the toast notifications.

### Steps to Fix the Error:

1. **Find the win10toast Directory**: Locate the `win10toast` directory inside your environment directory. This is typically found under `Lib\site-packages\win10toast` if you're using a virtual environment, or in your global Python `site-packages` directory.

2. **Modify `__init__.py`**: Open the `__init__.py` file within the `win10toast` directory for editing.

3. **Replace the `on_destroy` Function**: In the `__init__.py` file, find the `on_destroy` function and replace it with the following code:

    ```python
    def on_destroy(self, hwnd, msg, wparam, lparam):
        """Clean after notification ended.

        See https://learn.microsoft.com/en-us/windows/win32/winmsg/wm-destroy#return-value
        :hwnd:
        :msg:
        :wparam:
        :lparam:
        """
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)

        return 0
    ```

    This code is adapted from a pull request on the win10toast GitHub repository, specifically [pull request #115](https://github.com/jithurjacob/Windows-10-Toast-Notifications/pull/115/files).

4. **Save Changes**: After replacing the function, save the changes to the `__init__.py` file.

5. **Restart the App**: Close and restart the A&W Burger Deal Notification App to ensure the changes take effect.

## Additional Information

- It's always a good practice to back up the original `__init__.py` file before making any changes.
- Ensure that your Python environment has the necessary permissions to modify the files in the `site-packages` directory.

By following these steps, you should be able to resolve the `TypeError` and ensure that the notification functionality of the A&W Burger Deal Notification App works correctly.
