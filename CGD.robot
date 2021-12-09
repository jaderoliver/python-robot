***** Settings *****
Documentation     *Test Suite:* Navigate On CGD
...
...               *Objective:* Tests demonstartive of navigation on CGD application.
Resource          lib/CGD_KW.robot
Library           bin/Cgd.py    ${HOST}    ${BROWSER}    ${DEVICE}
Library           SeleniumLibrary

*** Test Cases ***
TC1
    [Documentation]    *Title:* TC1
    ...
    ...    *Description:* Test case to use as an example with navigations through CGD page.
    ...
    ...    *Input Arguments:* N/A
    ...
    ...    *Output Arguments:* N/A
    [Tags]    DEV
    [Setup]    Open application
    Open drop down menu "Poupanca e Investimento"
    Capture Page Screenshot
    Select Option "Simulador PPR" In Drop Down Menu
    Wait Page "Simulador PPR" to Open
    Capture Page Screenshot
    Input "99" In Field Box "Idade Atual"
    Input "100" In Field Box "Idade Expectavel de Reembolso"
    Input "1500" In Field Box "Montante da Subscricao Inicial"
    Input "100" In Field Box "Montante dos Reforcos Periodicos"
    Capture Page Screenshot
    Verify Value "1 016 515,00 €" Of "Valor Bruto Acumulado" In Page "Simulador PPR"
    Capture Page Screenshot
    Open drop down menu "Contas"
    Select Option "Conta Caixa" In Drop Down Menu
    Wait Page "Conta Caixa" to Open
    Dismiss Cookies
    Capture Page Screenshot
    Select Section "Conta Caixa S" Of Page "Conta Caixa"
    Select Section "Produtos para o dia-a-dia" Of Page "Conta Caixa"
    Select Section "Descontos e Vantagens" Of Page "Conta Caixa"
    Capture Page Screenshot
    Select Section "Conta Caixa M" Of Page "Conta Caixa"
    Select Section "Produtos para o dia-a-dia" Of Page "Conta Caixa"
    Select Section "Descontos e Vantagens" Of Page "Conta Caixa"
    Capture Page Screenshot
    Select Section "Conta Caixa L" Of Page "Conta Caixa"
    Select Section "Produtos para o dia-a-dia" Of Page "Conta Caixa"
    Select Section "Descontos e Vantagens" Of Page "Conta Caixa"
    Capture Page Screenshot
    [Teardown]    Close All Browsers
