# Switching App Mode from Development to Live for a Facebook App

## Overview

Facebook apps are initially set to "Development" mode by default to ensure that the apps are properly tested and debugged before being accessible to the public. When your app is ready to go live, you need to switch the app mode from "Development" to "Live". However, there are a few pre-requisites to be completed before switching the mode.

## Pre-requisites

Before making your app live, please ensure to complete the following:

1. **Testing**: Ensure that your app has been thoroughly tested for all possible use cases and scenarios to prevent any bugs or crashes once the app goes live.

2. **Privacy Policy URL**: Facebook requires all apps to have a valid privacy policy. Please make sure you have a valid privacy policy URL entered in your app settings.

3. **App Details**: Complete all app details in the settings, including app icons, contact email, and category.

4. **App Review**: If your app uses permissions and features other than the basic permissions, you will need to submit your app for App Review before it can go live.

5. **Terms and Conditions**: Ensure that you've complied with all Facebook's Platform Policies and Developer Policies.

6. **OAuth settings**: Make sure you've set the correct OAuth redirect URIs.

## Steps

1. **Login to your Facebook account**

   Make sure you're using the account that has administrative access to the Facebook App.

2. **Navigate to Facebook Developers**

   Go to [Facebook Developers](https://developers.facebook.com/) and click on "My Apps" in the top right corner.

3. **Select your app**

   From the dropdown list, select the app that you want to switch from Development to Live.

4. **Go to App Dashboard**

   Once you're in the app's dashboard, locate the 'Settings' tab on the left side of the screen.

5. **Switch to Live mode**

   In the top of the Settings panel, you will see your app's current mode. If it's set to 'Development', click the switch to move it to 'Live' mode.

6. **Confirm your decision**

   You'll be prompted to confirm the change. Once you confirm, your app will be live.

7. **Review settings**

   After switching your app to Live mode, make sure that all the settings are configured properly. Check that the right APIs are enabled, the appropriate permissions are granted, and your app is correctly linked to your website or platform.

## Things to Note

- Remember, making your app Live means it can interact with the public and all Facebook users (based on the permissions it has). Make sure it's thoroughly tested in Development mode before making this switch.
- Even after switching to Live mode, you can still make changes to your app settings. However, some changes may require your app to be reviewed by Facebook before they take effect.

## Conclusion

Switching your Facebook App from Development to Live mode is a straightforward process. It's essential to ensure that your app is fully functional and meets all of Facebook's guidelines and policies before making this switch.

For more information, refer to the [Facebook Developer Documentation](https://developers.facebook.com/docs/apps/).