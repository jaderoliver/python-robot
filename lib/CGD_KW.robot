*** Settings ***
Library           SeleniumLibrary
Library           Dialogs
Library           ../bin/Cgd.py    ${HOST}    ${BROWSER}    ${DEVICE}
Variables         GUI_data.py
Library           Collections

*** Variables ***
${HOST}           https://www.cgd.pt/Particulares/Pages/Particulares_v2.aspx
${BROWSER}        Chrome
${MOBILE_SERVER}    http://10.12.45.1:4444/wd/hub
${DEVICE}         None
${VIDEO}          ${False}

*** Keywords ***
Open Application
    [Documentation]    *Title:*
    ...    Open Application
    ...
    ...    *Description:*
    ...    This keyword allows to start the application in the desired HOST.
    ...
    ...    *Input Arguments:* N/A
    ...
    ...    *Output Arguments:* N/A
    Run Keyword Unless    '${DEVICE}' is 'None'    Create Safari Webdriver
    Run Keyword Unless    '${DEVICE}' is 'None'    Go to    ${HOST}
    Run Keyword If    '${DEVICE}' is 'None'    Open Browser    ${HOST}    browser=${BROWSER}    remote_url=10.244.1.143:4444
    Run Keyword If    '${DEVICE}' is 'None'    Maximize Browser Window
    Wait Locator    //h1[text()='Caixa Geral de Depósitos']    type=visible
    Run Keyword If    '${DEVICE}' is 'None' and ${VIDEO}    Start Recording    ffmpeg_exe_file_path=ffmpeg.exe

Open drop down menu "${menu}"
    [Documentation]    *Title:* Open drop down menu "${menu}"
    ...
    ...    *Description:* This keyword allows to open a specific menu in the drop down.
    ...
    ...    *Input Arguments:*
    ...    | *Argument* | *Mandatory* | *Summary* | *Values* | *Default* |
    ...    | menu | yes | Name of the menu to open | <string> | N/A |
    ...
    ...    *Output Arguments:* N/A
    ...
    ...    *Examples:*
    ...    | Open drop down menu "Poupanca e Investimento" |
    ${menu}=    Set Variable    ${menu.lower().replace(' ','_')}
    Click    ${main_menu.${menu}}
    Wait    ${main_page.menu_opened}
    Sleep    1

Select Option "${option}" In Drop Down Menu
    ${option}=    Set Variable    ${option.lower().replace(' ','_')}
    ${page}=    Set Variable
    ${option_locator}=    Replace Variables    ${drop_down_menu.${option}.id}
    Wait Locator    ${option_locator}
    Set Focus To Element    ${option_locator}
    Click Locator    ${option_locator}

Input "${text}" In Field Box "${field}"
    ${field}=    Set Variable    ${field.lower().replace(' ','_')}
    Write    ${simulador_ppr.${field}}    ${text}

Verify Value "${value}" Of "${field}" In Page "${page}"
    ${page}=    Set Variable    ${page.lower().replace(' ','_')}
    ${field}=    Set Variable    ${field.lower().replace(' ','_')}
    Wait Until Element Is Visible    ${${page}.${field}.id}
    Scroll Element Into View    ${${page}.${field}.id}
    Sleep    2
    ${displayed_value}=    Get Element Text    ${${page}.${field}}
    ${expected_value}=    Set Variable    ${value}
    Should Be Equal    ${displayed_value}    ${expected_value}

Wait Page "${page}" to Open
    ${page}=    Set Variable    ${page.lower().replace(' ','_')}
    Wait Locator    ${${page}.title.id}

Dismiss Cookies
    Click    ${main_page.dismiss_cookies}
    Wait    ${main_page.dismiss_cookies}    type_el=~visible

Select Section "${section}" Of Page "${page}"
    ${section}=    Set Variable    ${section.lower().replace(' ','_').replace('-','_')}
    ${page}=    Set Variable    ${page.lower().replace(' ','_')}
    Wait Locator    ${${page}.${section}.id}
    Scroll Element Into View    ${${page}.${section}.id}
    Click Locator    ${${page}.${section}.id}
    Sleep    2
