#!/usr/bin/env python
# -*- coding: cp1252 -*-
"""
### =============================================
###  PROJECT: Fasenra
###  MODULE: Fasenra
###  DESCRIPTION: Fasenra Python KWs for RFW
###  VERSION: 1.0.1
###  DEVELOPER: Bruno Calado
###  TEAM: AVV
###  DATE: 23-01-2019
###  PRE-REQ: (see classes.py)
###  Copyright 2017 Altran
### =============================================
"""

############################
### --- IMPORTATIONS --- ###
############################
import robot.api
#from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
import re

#############################
### --- Fasenra CLASS --- ###
#############################

class Cgd(object):
    """
    Python KWs for CGD example
    Use: Import Cgd
    """
    def __init__ (self, browser='chrome', host='https://portal-dmdp-qa-1-18.test.aws.intelpharma.net', device=None):
        self.bi = BuiltIn()
        self.log = robot.api.logger
        try:
            self.output_folder = self.bi.get_variable_value("${OUTPUT DIR}")
        except:
            self.output_folder = os.getcwd()
        self.record_job = None
        self.host = host
        self.browser = browser
        self.device = device

    @property
    def sl(self):
        return self.bi.get_library_instance('SeleniumLibrary')
    
## Robot Keywords

    def create_safari_webdriver(self):
        """
        Creates a webdriver to Run tests on mobile Safari.\n
        \n
        *Input*\n
        N/A
        \n
        *Output*\n
        N/A
        \n
        *Example:*\n
        | Create Safari Webdriver |
        """
        device = self.bi.get_variable_value("${${DEVICE}}")
        capabilities = {'automationName' : device.automationName,
                          'browserName'  : device.browserName,
                          'deviceName'   : device.deviceName,
                          'platformName' : device.platformName,
                          'udid'         : device.udid,
                          'orientation'  : device.orientation }
        server = self.bi.get_variable_value("${MOBILE_SERVER}")
        self.sl.create_webdriver('Remote', desired_capabilities=capabilities, command_executor=server)

    def write(self, element, text, logged=True, timeout=10):
        """
        Wait _element_ to be visible and then write _text_ on _element_.\n
        \n
        *Syntax:*\n
        | Write | element=${login.password} | text=${password} |
        | Write | ${login.username} | ${username} |
        \n
        *Input*\n
        | *Argument* | *Mandatory* | *Summary*              | *Values*  | *Default* |
        | element    | Yes         | Element to be filled   | <Element> | N/A       |
        | text       | Yes         | Inputed Text           | <string>  | N/A       |
        | logged     | No          | Text Visibility in Log | <bool>    | True      |
        | timeout    | No          | Maximum waiting time   | <string>  | 10 sec    |
        \n
        *Output*\n
        N/A
        \n
        *Example:*\n
        | Write | ${login.username} | ${username} |
        | Write | element=${login.password} | text=${${user}.password} | logged=${False} | timeout=5 |
        """
        locator = self._replace_locator_variables(element.id)
        self.wait_locator(locator,type_el='visible', timeout=timeout)
        if logged:
            self.sl.input_text(locator, text)
        else:
            self.sl.input_password(locator, text)

    def write_locator(self, locator, text, logged=True, timeout=10):
        """
        Wait _locator_ to be visible and then write _text_ on _locator_.\n
        \n
        *Syntax:*\n
        | Write Locator | locator=${login.password.id} | text=${password} |
        \n
        *Input*\n
        | *Argument* | *Mandatory* | *Summary*              | *Values*  | *Default* |
        | locator    | Yes         | Locator to be filled   | <locator> | N/A       |
        | text       | Yes         | Inputed Text           | <string>  | N/A       |
        | logged     | No          | Text Visibility in Log | <bool>    | True      |
        | timeout    | No          | Maximum waiting time   | <string>  | 10 sec    |
        \n
        *Output*\n
        N/A
        \n
        *Example:*\n
        | Write Locator| ${login.username.id} | ${username} |
        | Write Locator| element=${login.password.id} | text=${${user}.password} | logged=${False} | timeout=5 |
        """
        locator = self._replace_locator_variables(locator)
        self.wait_locator(locator,type_el='visible', timeout=timeout)
        if logged:
            self.sl.input_text(locator, text)
        else:
            self.sl.input_password(locator, text)

    def click(self, element, timeout=20):
        """
        Wait _element_ to be visible and then click on _element_.\n
        The KW uses the _element.type_ to decide what kind of Click that must performe.\n
        \n
        *Syntax:*\n
        | Click | element=${login.submit} | timeout=5 |
        \n
        *Input*\n
        | Argument | Mandatory | Summary | Values | Default |
        | element | Yes | Element to be clicked | <Element> | N/A |
        | timeout | No | Maximum waiting time | <string> | 10 sec |
        \n
        *Output*\n
        | N/A |
        \n
        *Example:*\n
        | Click | ${login.submit} |
        | Click | element=${login.submit} | timeout=5 |
        """
        locator = self._replace_locator_variables(element.id)
        self.wait_locator(locator,type_el='visible', timeout=timeout)
        if element.type == 'button':
            self.sl.click_button(locator)
        elif element.type == 'img':
            self.sl.click_link(locator)
        elif element.type == 'img':
            self.sl.click_image(locator)
        elif element.type == 'link':
            self.sl.click_link(locator)
        else:
            self.sl.click_element(locator)

    def click_locator(self, locator, timeout=20):
        """
        Wait _locator_ to be visible and then click on _locator_.\n
        \n
        *Syntax:*\n
        | Click Locator | locator=${login.submit.id} | timeout=5 |
        \n
        *Input*\n
        | Argument | Mandatory | Summary | Values | Default |
        | locator | Yes | Locator to be clicked | <locator> | N/A |
        | timeout | No | Maximum waiting time | <string> | 10 sec |
        \n
        *Output*\n
        | N/A |
        \n
        *Example:*\n
        | Click Locator | ${login.submit.id} |
        | Click Locator | locator=${login.submit.id} | timeout=5 |
        | Click Locator | xpath=//button[text()='Log in'] |
        """
        locator = self._replace_locator_variables(locator)
        self.wait_locator(locator, type_el='element', timeout=timeout)
        status = self.bi.run_keyword_and_return_status("click_element", locator)
        if not status:
            locator = self.bi.replace_variables(locator.split('xpath=')[1])
            self.bi.run_keyword_and_ignore_error(self.sl.assign_id_to_element, locator)
            self.sl.execute_javascript('5document.getElementById("clickThis").click();')
            
    def wait(self, element, type_el='element', timeout=20):
        """
        Wait an _element_ according _type_.\n
        If _type=visible_ wait until the _element.id_ to be visible.\n
        If _type=~visible_ wait until the _element.id_ not to be visible.\n
        If _type=contains_ wait until the element contains _element.txt_.\n
        If _type=~contains_ wait until the element not contains _element.txt_.\n
        If _type=enable_ wait until the _element.id_ to be enable.\n
        If _type=element_ wait until the page contains _element.id_.\n
        If _type=~element_ wait until the page not contains _element.id_.\n
        \n
        *Syntax:*\n
        | Wait | ${login.submit}  | type=visible | timeout=5 |
        \n
        *Input*\n
        | *Argument* | *Mandatory* | *Summary*              | *Values*  | *Default* |
        | element    | Yes         | Element to be waited   | <Element> | N/A       |
        | type       | No          | Type of Waiting        | <string>  | element   |
        | timeout    | No          | Maximum waiting time   | <string>  | 10 sec    |
        \n
        *Output*\n
        N/A
        \n
        *Example:*\n
        | Wait | ${login.submit} |
        | Wait | element=${login.submit} | type=visible | timeout=5 |
        | Wait | element=${login.submit} | type=~contain |
        """
        locator = self._replace_locator_variables(element.id)
        if type_el.lower() == 'contains':
            self.sl.wait_until_page_contains(element.txt, timeout=timeout)
        elif type_el.lower() == '~contains':
            self.sl.wait_until_page_does_not_contain(element.txt, timeout=timeout)
        elif type_el.lower() == 'visible':
            self.sl.wait_until_element_is_visible(locator, timeout=timeout)
        elif type_el.lower() == '~visible':
            self.sl.wait_until_element_is_not_visible(locator, timeout=timeout)
        elif type_el.lower() == 'enable':
            self.sl.wait_until_element_is_enabled(locator, timeout=timeout)
        elif type_el.lower() == '~element':
            self.sl.wait_until_page_does_not_contain_element(locator, timeout=timeout)
        else: self.sl.wait_until_page_contains_element(locator, timeout=timeout)

    def wait_locator(self, locator, type_el='element', timeout=20):
        """
        Wait a _locator_ according _type_.\n
        If _type=visible_ wait until the _locator_ to be visible.\n
        If _type=~visible_ wait until the _locator_ not to be visible.\n
        If _type=contains_ wait until the page contains _locator_ text.\n
        If _type=~contains_ wait until the page not contains _locator_ text.\n
        If _type=enable_ wait until the _locator_ to be enable.\n
        If _type=element_ wait until the page contains _locator_.\n
        If _type=~element_ wait until the page not contains _locator_.\n
        \n
        *Syntax:*\n
        | Wait | ${login.submit}  | type=visible | timeout=5 |
        \n
        *Input*\n
        | *Argument* | *Mandatory* | *Summary*              | *Values*  | *Default* |
        | locator    | Yes         | Locator to be waited   | <locator> | N/A       |
        | type       | No          | Type of Waiting        | <string>  | element   |
        | timeout    | No          | Maximum waiting time   | <string>  | 10 sec    |
        \n
        *Output*\n
        N/A
        \n
        *Example:*\n
        | Wait locator | ${login.submit} |
        | Wait locator | locator=${login.submit} | type=visible | timeout=5 |
        | Wait locator | locator=${login.submit} | type=~contain |
        | Wait Locator | xpath=//button[text()='Log in'] |
        """
        locator = self._replace_locator_variables(locator)
        if type_el.lower() == 'contains':
            self.sl.wait_until_page_contains(locator, timeout=timeout)
        elif type_el.lower() == '~contains':
            self.sl.wait_until_page_does_not_contain(locator, timeout=timeout)
        elif type_el.lower() == 'visible':
            self.sl.wait_until_element_is_visible(locator, timeout=timeout)
        elif type_el.lower() == '~visible':
            self.sl.wait_until_element_is_not_visible(locator, timeout=timeout)
        elif type_el.lower() == 'enable':
            self.sl.wait_until_element_is_enabled(locator, timeout=timeout)
        elif type_el.lower() == '~element':
            self.sl.wait_until_page_does_not_contain_element(locator, timeout=timeout)
        else: self.sl.wait_until_page_contains_element(locator, timeout=timeout)

    def get_element_text(self, element, timeout=15):
        """
        Wait _element_ to be visible and then get _text_ on _element_.\n
        \n
        *Syntax:*\n
        | Get Box Text | element=${login.password} | timeout=5 |
        \n
        *Input*\n
        | Argument | Mandatory | Summary | Values | Default |
        | element | Yes | Element to be read | <Element> | N/A |
        | timeout | No | Maximum waiting time | <string> | 10 sec |
        \n
        *Output*\n
        | Argument | Summary | Values |
        | text | Text of input box _element_ | <string> |
        \n
        *Example:*\n
        | Get Box Text | ${login.username} |
        | Get Box Text | element=${login.password} | timeout=5 |
        """
        locator = self._replace_locator_variables(element.id)
        self.wait_locator(locator, type_el='element', timeout=timeout)
        text = self.sl.get_value(locator)
        if text is None:
            text = self.sl.get_text(locator)
        return text

    def get_locator_text(self, locator, timeout=10):
        """
        Wait _locator_ to be visible and then get _text_ on _locator_.\n
        \n
        *Syntax:*\n
        | Get Box Text Locator | locator=id=input_text_userName_Admin-UserForm | timeout=5 |
        \n
        *Input*\n
        | Argument | Mandatory | Summary | Values | Default |
        | locator | Yes | Locator to be read | <locator> | N/A |
        | timeout | No | Maximum waiting time | <string> | 10 sec |
        \n
        *Output*\n
        | Argument | Summary | Values |
        | text | Text of input box _locator_ | <string> |
        \n
        *Example:*\n
        | Get Box Text Locator | ${login.username.id} |
        | Get Box Text Locator | locator=id=input_text_userName_Admin-UserForm | timeout=5 |
        """
        locator = self._replace_locator_variables(locator)
        self.wait_locator(locator, type_el='element', timeout=timeout)
        text = self.sl.get_value(locator)
        if text is None:
            text = self.sl.get_text(locator)
        return text

    def set_radio_button(self, title, radio_label, timeout=10):
        """
        Wait radio button to be visible and then (un)check the radio button.\n
        \n
        *Syntax:*\n
        | Set Radio Button | Gender | Female |
        \n
        *Input*\n
        | Argument | Mandatory | Summary | Values | Default |
        | title | Yes | Title of group where the checkbox to be handled is. | <string> | N/A |
        | radio_label | Yes | Name of the property to set | <string> | N/A |
        | timeout | No | Maximum waiting time | <string> | 10 sec |
        \n
        *Output*\n
        | N/A |
        \n
        *Example:*\n
        | Set Radio Button | Gender | Female |
        | Set Radio Button | Gender | Male | timeout=5 |
        """
        group_radios = "//div[label[text()='%s']]" % title.upper()
        radio_button = group_radios + "//input[@value='%s']" % radio_label.upper()
        self.wait_locator(group_radios, type_el='visible', timeout=timeout)
        radio_name = self.sl.get_element_attribute(radio_button, 'name')
        if 'ng-valid-parse' not in self.sl.get_element_attribute(radio_button, 'class'):
            self.sl.focus(radio_button)
            self.sl.select_radio_button(radio_name, radio_label.upper())
            selected_radio = radio_button + "[contains(@class, 'ng-valid-parse')]"
            self.wait_locator(selected_radio, type_el='element', timeout=timeout)
            return "The radio button '%s' in '%s' was selected." % (radio_label, title)

    def check_radio_button_status(self, title, radio_label, timeout=10):
        """
        Wait radio button to be visible and then check the radio button status.\n
        \n
        *Syntax:*\n
        | Check Radio Button Status| Gender | Female |
        \n
        *Input*\n
        | Argument | Mandatory | Summary | Values | Default |
        | title | Yes | Title of group where the checkbox to be handled is. | <string> | N/A |
        | radio_label | Yes | Name of the property to set | <string> | N/A |
        | timeout | No | Maximum waiting time | <string> | 10 sec |
        \n
        *Output*\n
        | N/A |
        \n
        *Example:*\n
        | Set Radio Button | Gender | Female |
        | Set Radio Button | Gender | Male | timeout=5 |
        """
        group_radios = "//div[label[text()='%s']]" % title.upper()
        radio_button = group_radios + "//input[@value='%s']" % radio_label.upper()
        self.wait_locator(group_radios, type_el='visible', timeout=timeout)
        radio_name = self.sl.get_element_attribute(radio_button, 'name')
        if 'ng-valid-parse' in self.sl.get_element_attribute(radio_button, 'class'):
            self.bi.log("The radio button '%s' is selected for '%s'." % (radio_label.capitalize(), title.capitalize()))
        else:
            raise AssertionError("The radio button '%s' is not selected for '%s'." % (radio_label.capitalize(), title.capitalize()))

    def select_label_from_combobox(self, element, label, timeout=10):
        """
        Wait combobox to be visible and then select an item from it, according to it label\n
        \n
        *Syntax:*\n
        | Check Radio Button Status| Gender | Female |
        \n
        *Input*\n
        | Argument | Mandatory | Summary | Values | Default |
        | element | Yes | Combobox to be handled | <Element> | N/A |
        | label | Yes | Label to be selected | <string> | N/A |
        | timeout | No | Maximum waiting time | <string> | 10 sec |
        \n
        *Output*\n
        | N/A |
        \n
        *Example:*\n
        | Select Label From Combobox | ${leader_projs.newproj.users} | ${user_name} |
        | Select Label From Combobox | element=${leader_projs.newproj.users} | label=${user_name} | timeout=5 |
        """
        locator = self._replace_locator_variables(element.id)
        self.wait_locator(locator, type_el='visible', timeout=timeout)
        self.sl.focus(locator)
        self.sl.select_from_list_by_label(locator, label)

    def select_label_from_combobox_locator(self, locator, label, timeout=10):
        """
        Wait combobox to be visible and then select an item from it, according to it label\n
        \n
        *Syntax:*\n
        | Check Radio Button Status| Gender | Female |
        \n
        *Input*\n
        | Argument | Mandatory | Summary | Values | Default |
        | locator | Yes | Combobox to be handled | <locator> | N/A |
        | label | Yes | Label to be selected | <string> | N/A |
        | timeout | No | Maximum waiting time | <string> | 10 sec |
        \n
        *Output*\n
        | N/A |
        \n
        *Example:*\n
        | Select Label From Combobox Locator | ${leader_projs.newproj.users.id} | ${day} |
        | Select Label From Combobox Locator | locator=${leader_projs.newproj.users.id} | label=${day} | timeout=5 |
        """
        locator = self._replace_locator_variables(locator)
        self.wait_locator(locator, type_el='visible', timeout=timeout)
        self.sl.focus(locator)
        self.sl.select_from_list_by_label(locator, label)

    def set_checkbox(self, locator, action='check', timeout=10, error_message=None):
        """
        Verifies that the page contains the checkbox identified by ``locator`` and checks or unchecks a checkbox
        according to the ``action``. Default ``action`` is check.

        Default ``timeout`` for the locator is 5 seconds.

        The default error message can be overridden by setting ``error_message`` argument.

        *Available Actions:*
        | *Action* | *Description* |
        | check | Checks the checkbox identified by ``locator`` |
        | uncheck | Unchecks the checkbox identified by ``locator`` |

        *Examples:*
        | Set Checkbox | id=chkBox |
        | Set Checkbox | id=chkBox | action=uncheck |timeout=10 | error_message=My Error Message |
        """
        locator = self._replace_locator_variables(locator)
        self.sl.wait_until_page_contains_element(locator, timeout, error_message)
        valid_actions = {'check'   : self.sl.select_checkbox,
                         'uncheck' : self.sl.unselect_checkbox}
        action = action.lower().strip()
        if action in valid_actions.iterkeys(): valid_actions[action](locator)
        else: raise AssertionError('"' + str(action) + '" is an invalid action!')

    def verify_checkbox_state(self, locator, value='checked', timeout=5, error_message=None):
        """
        Verifies that the page contains the checkbox identified by ``locator`` and validates if the checkbox is checked
        or unchecked according to ``value``. Default ``value`` is checked.

        Default ``timeout`` for the locator is 5 seconds.

        The default error message can be overridden by setting ``error_message`` argument.

        *Available Values:*
        | *Value* | *Description* |
        | checked | Verifies if the checkbox identified by ``locator`` is checked |
        | unchecked | Verifies if the checkbox identified by ``locator`` unchecked |

        *Examples:*
        | Verify Checkbox State | id=chkBox |
        | Verify Checkbox State | id=chkBox | value=unchecked |timeout=10 | error_message=My Error Message |
        """
        self.sl.wait_until_page_contains_element(locator, timeout, error_message)
        valid_values = {'checked'   : self.sl.checkbox_should_be_selected,
                        'unchecked' : self.sl.checkbox_should_not_be_selected}
        value = value.lower().strip()
        if value in valid_values.iterkeys(): valid_values[value](locator)
        else: raise AssertionError('"' + str(value) + '" is an invalid action!')

    def start_recording(self, ffmpeg_exe_file_path=None, file_extension='mp4', framerate=30, verbose='quiet'):
        self.start_record(ffmpeg_exe_file_path, file_extension, framerate, verbose)

    def wait_operation(self, element, timeout=10):
        """
        Wait an operation to be completed.\n
        It waits the visibility of an _element_ (message) and then wait that _element_ (message) to disappear.\n
        \n
        *Input*\n
        | Argument | Mandatory | Summary | Values | Default |
        | element | Yes | Element to wait | <Element> | N/A |
        | timeout | No | Maximum waiting time | <string> | 10 sec |
        \n
        *Output*\n
        | N/A |
        \n
        *Examples:*
        | Wait Operation | ${statusbar.ok_msg} |
        | Wait Operation | element=${statusbar.ok_msg} | timeout=5 |
        """
        locator = self._replace_locator_variables(element.id)
        self.wait_locator(locator, type_el='element', timeout=timeout)
        self.wait_locator(locator, type_el='~element', timeout=timeout)

    def close_application(self, all_browsers=True, logout=True):
        """
        This keyword closes the application and collects all evidences (a video in every tests and a screenshot if test fails)\n
        \n
        *Input*\n
        | Argument | Mandatory | Summary | Values | Default |
        | all_browsers | No | True if it should close all opened browsers | <bool> | True |
        \n
        *Output*\n
        | N/A |
        \n
        *Examples:*
        | Close And Collect Evidence |
        | Close And Collect Evidence | all_browsers= False |
        """
        self.bi.run_keyword_if_test_failed('Page Screenshot')
        if logout:
            self.bi.run_keyword_and_ignore_error('Logout')
        if all_browsers:
            self.sl.close_all_browsers()
        else:
            self.sl.close_browser()

    def show_test_video(self):
        video= self.bi.get_variable_value("${${VIDEO}}")
        device = self.bi.get_variable_value("${${DEVICE}}")
        if device is None and video:
            self.stop_record()
            self.show_video()

## Private Keywords
        
    def _replace_locator_variables(self, locator):
        find_replacements = re.compile('\$\{[^\']+')
        if find_replacements.search(locator):
            locator = self.bi.replace_variables(locator)
        return locator
        
