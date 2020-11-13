#!/usr/bin/env python
# -*- coding: cp1252 -*-
"""
### =============================================
###  PROJECT: CGD
###  MODULE: GUI_data (Main)
###  DESCRIPTION: Data Model File
###  VERSION: 1.0.1
###  DEVELOPER:
###  TEAM: AVV
###  DATE: 10-01-2020
###  PRE-REQ: (see classes.py)
###  Copyright 2017 Altran
### =============================================
"""

############################
### --- IMPORTATIONS --- ###
############################
from classes import Page


#########################
### --- MAIN PAGE --- ###
#########################
main_page = Page('Main Page of CGD')
main_page.add(name="dismiss_cookies"                     , type="element" , locator="xpath=//a[@aria-label='dismiss cookie message']")
main_page.add(name="menu_opened"                         , type="element" , locator="xpath=//div[@id='menu3nivel'][contains(@class,'open')]")

#########################
### --- MAIN MENU --- ###
#########################
main_menu = Page('Main menu')
main_menu.add(name="poupanca_e_investimento"             , type="element" , locator="xpath=//li[@data-mid='PoupancaInvestimento']/a")
main_menu.add(name="contas"                              , type="element" , locator="xpath=//li[@data-mid='Contas']/a")
main_menu.add(name="imoveis"                             , type="element" , locator="xpath=//li[@data-mid='Imoveis']/a")

##############################
### --- DROP DOWN MENU --- ###
##############################
drop_down_menu = Page('Drop down menu')
drop_down_menu.add(name="simulador_ppr"                  , type="element" , locator="xpath=//div[contains(@class,'PoupancaInvestimento')]//li[text()='Ferramentas']//following-sibling::li//a[contains(.,'Simulador PPR')]")
drop_down_menu.add(name="conta_caixa"                    , type="element" , locator="xpath=//div[contains(@class,'Contas')]//li[text()='Contas']//following-sibling::li//a[text()='Conta Caixa']")
drop_down_menu.add(name="solucoes_condominio"            , type="element" , locator="xpath=//div[contains(@class,'Imoveis')]//li[contains(text(),'Condom')]//following-sibling::li//a[@title]")

#########################
### --- SIMULADOR --- ###
#########################
simulador_ppr = Page('Page of <<Simulador PPR>>')
simulador_ppr.add(name="title"                           , type="element" , locator="xpath=//h2[@class='title' and text()='Simulador']")
simulador_ppr.add(name="idade_atual"                     , type="element" , locator="xpath=//input[@id='idadeAtualInput']")
simulador_ppr.add(name="idade_expectavel_de_reembolso"   , type="element" , locator="xpath=//input[@id='idadeReembolsoInput']")
simulador_ppr.add(name="montante_da_subscricao_inicial"  , type="element" , locator="xpath=//input[@id='montanteInicialInput']")
simulador_ppr.add(name="montante_dos_reforcos_periodicos", type="element" , locator="xpath=//input[@id='montanteReforcoInput']")
simulador_ppr.add(name="valor_bruto_acumulado"           , type="element" , locator="xpath=//td[span[text()='Valor Bruto Acumulado']]//following-sibling::span[contains(@class,'text')]")

######################
### --- CONTAS --- ###
######################
conta_caixa = Page('Page of <<Conta Caixa>>')
conta_caixa.add(name="title"                             , type="element" , locator="xpath=//h2[@class='title' and contains(text(),'Caracter')]")
conta_caixa.add(name="conta_caixa_s"                     , type="element" , locator="xpath=//span[@class='level-S']")
conta_caixa.add(name="conta_caixa_m"                     , type="element" , locator="xpath=//span[@class='level-M']")
conta_caixa.add(name="conta_caixa_l"                     , type="element" , locator="xpath=//span[@class='level-L']")
conta_caixa.add(name="produtos_para_o_dia_a_dia"         , type="element" , locator="xpath=//div[@class='tabContent open']//div[text()='PRODUTOS PARA O DIA A DIA']")
conta_caixa.add(name="descontos_e_vantagens"             , type="element" , locator="xpath=//div[@class='tabContent open']//div[text()='DESCONTOS E VANTAGENS EM PARCEIROS']")

