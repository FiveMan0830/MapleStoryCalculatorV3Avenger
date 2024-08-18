from re import M
import sys
from PyQt5 import QtWidgets
from Character import Character
from Calculator_UI import Calculator_UI
import math

class AppWindow(QtWidgets.QDialog):
    # event: APP初始化
    def __init__(me):
        super().__init__()
        me.myUI = Calculator_UI()
        me.myUI.setupUi(me)

        me.loadUIConfig()
        me.show()

    # function: UI事件綁定
    def loadUIConfig(me):
        myCharacter = Character()
        myUI = me.myUI
        
        myUI.btnAbility_SelectFile.clicked.connect(me.doSelectFile)
        myUI.btnAbility_SaveFile.clicked.connect(me.doSaveFile)
        myUI.btnAbility_Submit.clicked.connect(me.doSubmit)

        # page: 角色參數
        myUI.viewParameter_RANGE_VALUE.textChanged.connect(me.calc_Equivalent)
        myUI.viewParameter_RANGE_TYPE.activated.connect(me.calc_Equivalent)

        myUI.viewParameter_IMPROVE_VALUE_STR_CLEAR.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_STR_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_STR_UNIQUE.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_HP_CLEAR.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_HP_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_HP_UNIQUE.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_ALL_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_ATT.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_ATT_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_DMG_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_BOSS_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_STRIKE_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_IGNORE_P.textChanged.connect(me.calc_Improve)
        myUI.viewParameter_IMPROVE_VALUE_AS_PARAMETER.activated.connect(me.calc_Improve)


        # page: 裝備變更
        myUI.viewEquipment_origin_STR.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_STR_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_HP.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_HP_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_ALL_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_ATTACK.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_ATTACK_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_DMG_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_STRIKE_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_origin_IGNORE_P.textChanged.connect(me.calc_Equipment)

        myUI.viewEquipment_Set1_STR.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_STR_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_HP.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_HP_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_ALL_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_ATTACK.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_ATTACK_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_DMG_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_STRIKE_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set1_IGNORE_P.textChanged.connect(me.calc_Equipment)

        myUI.viewEquipment_Set2_STR.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_STR_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_HP.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_HP_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_ALL_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_ATTACK.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_ATTACK_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_DMG_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_STRIKE_P.textChanged.connect(me.calc_Equipment)
        myUI.viewEquipment_Set2_IGNORE_P.textChanged.connect(me.calc_Equipment)

        # page: 工具
        myUI.btnTools_IGNORE_SUBMIT.clicked.connect(me.doCalcIgnore)
        
        me.myCharacter = myCharacter
        pass
    
    # event: 更新職業對應資訊
    def updateClassInfo(me):
        myCharacter = me.myCharacter
        myUI = me.myUI

        CLASS_INFO = myCharacter.getInfo()
        myUI.viewAbility_WP.setCurrentIndex(CLASS_INFO['WP_IDX'])
        # print(CLASS_INFO)
        pass

    # event: 選擇檔案
    def doSelectFile(me):
        try:
            fileName, filetype = QtWidgets.QFileDialog.getOpenFileName(me,'選擇檔案', './', 'txt (*.txt)')
            data = open(fileName, 'r')

            myUI = me.myUI
            for row in iter(data):
                item = row.replace('\n','').split('=')
                # print(item)

                if (item[0] == 'LEVEL'): myUI.viewAbility_LEVEL.setText(item[1])
                if (item[0] == 'ATTACK'): myUI.viewAbility_ATTACK.setText(item[1])
                if (item[0] == 'ATTACK_P'): myUI.viewAbility_ATTACK_P.setText(item[1])
                if (item[0] == 'DMG_P'): myUI.viewAbility_DMG_P.setText(item[1])
                if (item[0] == 'BOSS_P'): myUI.viewAbility_BOSS_P.setText(item[1])
                if (item[0] == 'STRIKE_P'): myUI.viewAbility_STRIKE_P.setText(item[1])
                if (item[0] == 'IGNORE_P'): myUI.viewAbility_IGNORE_P.setText(item[1])
                if (item[0] == 'FINALDMG_P'): myUI.viewAbility_FINALDMG_P.setText(item[1])
                if (item[0] == 'DEFENSE_P'): myUI.viewAbility_DEFENSE_P.setText(item[1])
                
                if (item[0] == 'STR_CLEAR'): myUI.viewAbility_STR_CLEAR.setText(item[1])
                if (item[0] == 'STR_P'): myUI.viewAbility_STR_P.setText(item[1])
                if (item[0] == 'STR_UNIQUE'): myUI.viewAbility_STR_UNIQUE.setText(item[1])

                if (item[0] == 'HP_CLEAR'): myUI.viewAbility_HP_CLEAR.setText(item[1])
                if (item[0] == 'HP_P'): myUI.viewAbility_HP_P.setText(item[1])
                if (item[0] == 'HP_UNIQUE'): myUI.viewAbility_HP_UNIQUE.setText(item[1])
            
            data.close()
            me.doSubmit()
        except Exception:
            pass    
    
    # event: 儲存檔案
    def doSaveFile(me):
        try:
            fileName, filetype = QtWidgets.QFileDialog.getSaveFileName(me,'另存新檔','./','txt (*.txt)')
            data = open(fileName, 'w')
            myUI = me.myUI
            array = [
                'LEVEL=' + str(myUI.viewAbility_LEVEL.text()) + '\n',
                'ATTACK=' + str(myUI.viewAbility_ATTACK.text()) + '\n',
                'ATTACK_P=' + str(myUI.viewAbility_ATTACK_P.text()) + '\n',
                'DMG_P=' + str(myUI.viewAbility_DMG_P.text()) + '\n',
                'BOSS_P=' + str(myUI.viewAbility_BOSS_P.text()) + '\n',
                'STRIKE_P=' + str(myUI.viewAbility_STRIKE_P.text()) + '\n',
                'IGNORE_P=' + str(myUI.viewAbility_IGNORE_P.text()) + '\n',
                'FINALDMG_P=' + str(myUI.viewAbility_FINALDMG_P.text()) + '\n',
                'DEFENSE_P=' + str(myUI.viewAbility_DEFENSE_P.text()) + '\n',
                
                'STR_CLEAR=' + str(myUI.viewAbility_STR_CLEAR.text()) + '\n',
                'STR_P=' + str(myUI.viewAbility_STR_P.text()) + '\n',
                'STR_UNIQUE=' + str(myUI.viewAbility_STR_UNIQUE.text()) + '\n',

                'HP_CLEAR=' + str(myUI.viewAbility_HP_CLEAR.text()) + '\n',
                'HP_P=' + str(myUI.viewAbility_HP_P.text()) + '\n',
                'HP_UNIQUE=' + str(myUI.viewAbility_HP_UNIQUE.text()) + '\n',
            ]

            data.writelines(array)
            data.close()
        except Exception:
            pass    
    
    # event: 送出資料
    def doSubmit(me):
        try:
            myCharacter = me.myCharacter
            myUI = me.myUI
            myCharacter.reset()

            data = {
                'LEVEL': myUI.textToInt(myUI.viewAbility_LEVEL.text()),
                'ATTACK': myUI.textToInt(myUI.viewAbility_ATTACK.text()),
                'ATTACK_P': myUI.textToFloat(myUI.viewAbility_ATTACK_P.text()) / 100,
                'DMG_P': myUI.textToFloat(myUI.viewAbility_DMG_P.text()) / 100,
                'BOSS_P': myUI.textToFloat(myUI.viewAbility_BOSS_P.text()) / 100,
                'STRIKE_P': myUI.textToFloat(myUI.viewAbility_STRIKE_P.text()) / 100,
                'IGNORE_P': myUI.textToFloat(myUI.viewAbility_IGNORE_P.text()) / 100,
                'FINALDMG_P': myUI.textToFloat(myUI.viewAbility_FINALDMG_P.text()) / 100,
                'DEFENSE_P': myUI.textToInt(myUI.viewAbility_DEFENSE_P.text()) / 100,

                'STR_CLEAR': myUI.textToInt(myUI.viewAbility_STR_CLEAR.text()),
                'STR_P': myUI.textToInt(myUI.viewAbility_STR_P.text())/100,
                'STR_UNIQUE': myUI.textToInt(myUI.viewAbility_STR_UNIQUE.text()),

                'HP_CLEAR': myUI.textToInt(myUI.viewAbility_HP_CLEAR.text()),
                'HP_P': myUI.textToInt(myUI.viewAbility_HP_P.text())/100,
                'HP_UNIQUE': myUI.textToInt(myUI.viewAbility_HP_UNIQUE.text()),
            }

            myCharacter.updateAbilityByData(data)
            print('me.calc_Equivalent()')
            me.calc_Equivalent()
            print('me.calc_Improve()')
            me.calc_Improve()
            print('me.calc_Equipment()')
            me.calc_Equipment()
            QtWidgets.QMessageBox.information(me, '提示', '計算完成')
        except Exception as e:
            QtWidgets.QMessageBox.warning(me, '提示', '輸入資料有誤')
            print('doSubmit')
            print(e)
            pass

    # event: 計算等效數值
    def calc_Equivalent(me):
        try:
            myCharactor = me.myCharacter
            myUI = me.myUI
            
            if (myCharactor.isReset): return False
            
            RANGE_VALUE = myUI.textToFloat(myUI.viewParameter_RANGE_VALUE.text())
            RANGE_TYPE = myUI.viewParameter_RANGE_TYPE.currentText().replace('　', '').replace(' ', '').replace('=', '')
            
            new_data = {}

            if(RANGE_TYPE == '攻擊'):
                new_data['ATTACK'] = RANGE_VALUE
            
            if(RANGE_TYPE == '％攻擊'): 
                new_data['ATTACK_P'] = RANGE_VALUE / 100
                
            if(RANGE_TYPE == '％總傷'): 
                new_data['DMG_P'] = RANGE_VALUE / 100
                
            if(RANGE_TYPE == '％Ｂ傷'): 
                new_data['BOSS_P'] = RANGE_VALUE / 100
            
            if(RANGE_TYPE == '％爆傷'): 
                new_data['STRIKE_P'] = RANGE_VALUE / 100
                
            if(RANGE_TYPE == '％無視'):
                new_data['IGNORE_P'] = RANGE_VALUE / 100

            if(RANGE_TYPE == '％全屬'): 
                new_data['STR_P'] = RANGE_VALUE / 100
                
            if(RANGE_TYPE == '力量'): 
                new_data['STR_CLEAR'] = RANGE_VALUE
                
            if(RANGE_TYPE == '％力量'): 
                new_data['STR_P'] = RANGE_VALUE / 100
            
            if(RANGE_TYPE == '不吃％力'): 
                new_data['STR_UNIQUE'] = RANGE_VALUE

            if(RANGE_TYPE == 'HP'): 
                new_data['HP_CLEAR'] = RANGE_VALUE
                
            if(RANGE_TYPE == '％HP'): 
                new_data['HP_P'] = RANGE_VALUE / 100
            
            if(RANGE_TYPE == '不吃％HP'): 
                new_data['HP_UNIQUE'] = RANGE_VALUE

            IMPROVE_INFO = myCharactor.calcImprove(new_data)

            STATE_INFO = myCharactor.getEquivalent(IMPROVE_INFO['TOTAL'])

            def toRoundStr(value): 
                return str(round(value,3))
            
            myUI.viewParameter_EQUIVALENT_ALL_P.setText(toRoundStr(STATE_INFO['ALL_P']*100))
            myUI.viewParameter_EQUIVALENT_Att.setText(toRoundStr(STATE_INFO['ATTACK']))
            myUI.viewParameter_EQUIVALENT_Att_P.setText(toRoundStr(STATE_INFO['ATTACK_P']*100))
            myUI.viewParameter_EQUIVALENT_Dmg_P.setText(toRoundStr(STATE_INFO['DMG_P']*100))
            myUI.viewParameter_EQUIVALENT_Boss_P.setText(toRoundStr(STATE_INFO['BOSS_P']*100))
            myUI.viewParameter_EQUIVALENT_Strike_P.setText(toRoundStr(STATE_INFO['STRIKE_P']*100))
            myUI.viewParameter_EQUIVALENT_Ignore_P.setText(toRoundStr(STATE_INFO['IGNORE_P']*100))
            
            myUI.viewParameter_EQUIVALENT_STR_CLEAR.setText(toRoundStr(STATE_INFO['STR_CLEAR']))
            myUI.viewParameter_EQUIVALENT_STR_P.setText(toRoundStr(STATE_INFO['STR_P']*100))
            myUI.viewParameter_EQUIVALENT_STR_UNIQUE.setText(toRoundStr(STATE_INFO['STR_UNIQUE']))
            
            myUI.viewParameter_EQUIVALENT_HP_CLEAR.setText(toRoundStr(STATE_INFO['HP_CLEAR']))
            myUI.viewParameter_EQUIVALENT_HP_P.setText(toRoundStr(STATE_INFO['HP_P']*100))
            myUI.viewParameter_EQUIVALENT_HP_UNIQUE.setText(toRoundStr(STATE_INFO['HP_UNIQUE']))

        except Exception as e:
            QtWidgets.QMessageBox.warning(me, '提示', '輸入資料有誤')
            print('calc_equi')
            print(e)
            pass

    # event: 計算增幅
    def calc_Improve(me):
        try:
            myCharactor = me.myCharacter
            myUI = me.myUI

            if (myCharactor.isReset): return False
            new_data = {
                'DMG_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_DMG_P.text()) / 100,
                'BOSS_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_BOSS_P.text()) / 100,
                'ATTACK': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_ATT.text()),
                'ATTACK_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_ATT_P.text()) / 100,
                'STRIKE_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_STRIKE_P.text()) / 100,
                'IGNORE_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_IGNORE_P.text()) / 100,

                'STR_CLEAR': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_STR_CLEAR.text()),
                'STR_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_STR_P.text()) / 100,
                'STR_UNIQUE': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_STR_UNIQUE.text()),

                'HP_CLEAR': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_HP_CLEAR.text()),
                'HP_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_HP_P.text()) / 100,
                'HP_UNIQUE': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_HP_UNIQUE.text()),

                'ALL_P': myUI.textToFloat(myUI.viewParameter_IMPROVE_VALUE_ALL_P.text()) / 100,
            }

            IMPROVE_INFO = myCharactor.calcImprove(new_data)
            ESTIMATE_INFO = myCharactor.getEstimate(new_data)

            def toPercentText(value): 
                return str(round((value-1)*100,2)) + '%'

            IMPROVE_TEXT = '增幅 '
            myUI.viewParameter_IMPROVE_STR_CLEAR.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['STR_CLEAR']))
            myUI.viewParameter_IMPROVE_STR_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['STR_P']))
            myUI.viewParameter_IMPROVE_STR_UNIQUE.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['STR_UNIQUE']))
            
            myUI.viewParameter_IMPROVE_HP_CLEAR.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['HP_CLEAR']))
            myUI.viewParameter_IMPROVE_HP_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['HP_P']))
            myUI.viewParameter_IMPROVE_HP_UNIQUE.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['HP_UNIQUE']))

            myUI.viewParameter_IMPROVE_ALL_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['ALL_P']))

            myUI.viewParameter_IMPROVE_ATT.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['ATTACK']))
            myUI.viewParameter_IMPROVE_ATT_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['ATTACK_P']))
            myUI.viewParameter_IMPROVE_DMG_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['DMG_P']))
            myUI.viewParameter_IMPROVE_BOSS_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['BOSS_P']))
            myUI.viewParameter_IMPROVE_STRIKE_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['STRIKE_P']))
            myUI.viewParameter_IMPROVE_IGNORE_P.setText(IMPROVE_TEXT + toPercentText(IMPROVE_INFO['IGNORE_P']))

            myUI.viewParameter_IMPROVE_Total.setText('總增幅 ' + toPercentText(IMPROVE_INFO['TOTAL']))

            STATE_INFO = myCharactor.getEquivalent(IMPROVE_INFO['TOTAL'])
            RANGE_TYPE = myUI.viewParameter_IMPROVE_VALUE_AS_PARAMETER.currentText().replace('　', '').replace(' ', '')
            
            def toFloorStr(value): 
                return str(math.floor(value))

            PREFIX_TXT = '等同於 增加 '
            
            if(RANGE_TYPE == '攻擊'):
                myUI.viewParameter_IMPROVE_VALUE_AS.setText(PREFIX_TXT + str(round(STATE_INFO['ATTACK'],3)))
            
            if(RANGE_TYPE == '％攻擊'): 
                myUI.viewParameter_IMPROVE_VALUE_AS.setText(PREFIX_TXT + str(round(STATE_INFO['ATTACK_P']*100,3)))
            
            if(RANGE_TYPE == '％總傷'): 
                myUI.viewParameter_IMPROVE_VALUE_AS.setText(PREFIX_TXT + str(round(STATE_INFO['DMG_P']*100,3)))
            
            if(RANGE_TYPE == '％Ｂ傷'): 
                myUI.viewParameter_IMPROVE_VALUE_AS.setText(PREFIX_TXT + str(round(STATE_INFO['BOSS_P']*100,3)))
            
            if(RANGE_TYPE == '％爆傷'): 
                myUI.viewParameter_IMPROVE_VALUE_AS.setText(PREFIX_TXT + str(round(STATE_INFO['STRIKE_P']*100,3)))
            
            if(RANGE_TYPE == '％無視'):
                myUI.viewParameter_IMPROVE_VALUE_AS.setText(PREFIX_TXT + str(round(STATE_INFO['IGNORE_P']*100,3)))
            
            if(RANGE_TYPE == '％全屬'): 
                myUI.viewParameter_IMPROVE_VALUE_AS.setText(PREFIX_TXT + str(round(STATE_INFO['ALL_P']*100,3)))
            
            if(RANGE_TYPE == '力量'): 
                myUI.viewParameter_IMPROVE_VALUE_AS.setText(PREFIX_TXT + str(round(STATE_INFO['STR_CLEAR'],3)))
            
            if(RANGE_TYPE == '％力量'): 
                myUI.viewParameter_IMPROVE_VALUE_AS.setText(PREFIX_TXT + str(round(STATE_INFO['STR_P']*100,3)))
            
            if(RANGE_TYPE == '不吃％力'): 
                myUI.viewParameter_IMPROVE_VALUE_AS.setText(PREFIX_TXT + str(round(STATE_INFO['STR_UNIQUE'],3)))

            if(RANGE_TYPE == 'HP'): 
                myUI.viewParameter_IMPROVE_VALUE_AS.setText(PREFIX_TXT + str(round(STATE_INFO['HP_CLEAR'],3)))
            
            if(RANGE_TYPE == '％HP'): 
                myUI.viewParameter_IMPROVE_VALUE_AS.setText(PREFIX_TXT + str(round(STATE_INFO['HP_P']*100,3)))
            
            if(RANGE_TYPE == '不吃％HP'): 
                myUI.viewParameter_IMPROVE_VALUE_AS.setText(PREFIX_TXT + str(round(STATE_INFO['HP_UNIQUE'],3)))

            # 預估值
            myUI.viewParameter_ESTIMATE_STR.setText(toFloorStr(ESTIMATE_INFO['STR']))
            myUI.viewParameter_ESTIMATE_STR_P.setText(toFloorStr(ESTIMATE_INFO['STR_P']*100))
            
            myUI.viewParameter_ESTIMATE_HP.setText(toFloorStr(ESTIMATE_INFO['HP']))
            myUI.viewParameter_ESTIMATE_HP_P.setText(toFloorStr(ESTIMATE_INFO['HP_P']*100))

            myUI.viewParameter_ESTIMATE_ATTACK.setText(toFloorStr(ESTIMATE_INFO['ATTACK']))
            myUI.viewParameter_ESTIMATE_ATTACK_P.setText(str(round(ESTIMATE_INFO['ATTACK_P']*100)))

            myUI.viewParameter_ESTIMATE_DMG_P.setText(str(round(ESTIMATE_INFO['DMG_P']*100,2)))
            myUI.viewParameter_ESTIMATE_BOSS_P.setText(str(round(ESTIMATE_INFO['BOSS_P']*100,2)))

            myUI.viewParameter_ESTIMATE_STRIKE_P.setText(str(round(ESTIMATE_INFO['STRIKE_P']*100,2)))
            myUI.viewParameter_ESTIMATE_IGNORE_P.setText(str(round(ESTIMATE_INFO['IGNORE_P']*100,2)))
        except Exception as e:
            QtWidgets.QMessageBox.warning(me, '提示', '輸入資料有誤')
            print('calc_imp')
            print(e)
            pass

    # function: 計算裝備更換
    def calc_Equipment(me):
        try:
            myCharactor = me.myCharacter
            myUI = me.myUI

            if (myCharactor.isReset): return False
            def getData():
                new_data = {
                    'DMG_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_DMG_P.text()) / 100),
                    'ATTACK': 0 - myUI.textToFloat(myUI.viewEquipment_origin_ATTACK.text()),
                    'ATTACK_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_ATTACK_P.text()) / 100),
                    'STRIKE_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_STRIKE_P.text()) / 100),
                    'IGNORE_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_IGNORE_P.text()) / 100),

                    'STR_CLEAR': 0 - myUI.textToFloat(myUI.viewEquipment_origin_STR.text()),
                    'STR_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_STR_P.text()) / 100),

                    'HP_CLEAR': 0 - myUI.textToFloat(myUI.viewEquipment_origin_HP.text()),
                    'HP_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_HP_P.text()) / 100),

                    'ALL_P': 0 - (myUI.textToFloat(myUI.viewEquipment_origin_ALL_P.text()) / 100)
                }
                return new_data

            def toPercentText(value):
                return str(round((value-1) * 100,2)) + '%'

            SET_INFO = getData()
            SET_INFO['DMG_P'] += (myUI.textToFloat(myUI.viewEquipment_Set1_DMG_P.text())/100)
            SET_INFO['ATTACK'] += myUI.textToFloat(myUI.viewEquipment_Set1_ATTACK.text())
            SET_INFO['ATTACK_P'] += (myUI.textToFloat(myUI.viewEquipment_Set1_ATTACK_P.text())/100)
            SET_INFO['STRIKE_P'] += (myUI.textToFloat(myUI.viewEquipment_Set1_STRIKE_P.text())/100)
            SET_INFO['STR_CLEAR'] += myUI.textToFloat(myUI.viewEquipment_Set1_STR.text())
            SET_INFO['STR_P'] += (myUI.textToFloat(myUI.viewEquipment_Set1_STR_P.text())/100)
            SET_INFO['HP_CLEAR'] += myUI.textToFloat(myUI.viewEquipment_Set1_HP.text())
            SET_INFO['HP_P'] += (myUI.textToFloat(myUI.viewEquipment_Set1_HP_P.text())/100)
            SET_INFO['ALL_P'] += (myUI.textToFloat(myUI.viewEquipment_Set1_ALL_P.text())/100)
            
            # 重算等效無視
            IGNORE_TO = myCharactor.calcIgnore(myCharactor.getData()['IGNORE_P'], SET_INFO['IGNORE_P'])
            IGNORE_TO = myCharactor.calcIgnore(IGNORE_TO, (myUI.textToFloat(myUI.viewEquipment_Set1_IGNORE_P.text())/100))
            SET_INFO['IGNORE_P'] = 0
            if (IGNORE_TO > myCharactor.getData()['IGNORE_P']):
                SET_INFO['IGNORE_P'] = 1 - ((1 - IGNORE_TO) / (1 - myCharactor.getData()['IGNORE_P']))
            if (IGNORE_TO < myCharactor.getData()['IGNORE_P']):
                SET_INFO['IGNORE_P'] = ((1 - myCharactor.getData()['IGNORE_P']) / (1 - IGNORE_TO)) - 1
            
            # 計算加總
            IMPROVE_INFO = myCharactor.calcImprove(SET_INFO)
            myUI.viewEquipment_Set1_IMPROVE.setText('增幅 ' + str(toPercentText(IMPROVE_INFO['TOTAL'])))

            SET_INFO = getData()
            SET_INFO['DMG_P'] += (myUI.textToFloat(myUI.viewEquipment_Set2_DMG_P.text())/100)
            SET_INFO['ATTACK'] += myUI.textToFloat(myUI.viewEquipment_Set2_ATTACK.text())
            SET_INFO['ATTACK_P'] += (myUI.textToFloat(myUI.viewEquipment_Set2_ATTACK_P.text())/100)
            SET_INFO['STRIKE_P'] += (myUI.textToFloat(myUI.viewEquipment_Set2_STRIKE_P.text())/100)
            SET_INFO['STR_CLEAR'] += myUI.textToFloat(myUI.viewEquipment_Set2_STR.text())
            SET_INFO['STR_P'] += (myUI.textToFloat(myUI.viewEquipment_Set2_STR_P.text())/100)
            SET_INFO['HP_CLEAR'] += myUI.textToFloat(myUI.viewEquipment_Set2_HP.text())
            SET_INFO['HP_P'] += (myUI.textToFloat(myUI.viewEquipment_Set2_HP_P.text())/100)
            SET_INFO['ALL_P'] += (myUI.textToFloat(myUI.viewEquipment_Set2_ALL_P.text())/100)
            
            IGNORE_TO = myCharactor.calcIgnore(myCharactor.getData()['IGNORE_P'], SET_INFO['IGNORE_P'])
            IGNORE_TO = myCharactor.calcIgnore(IGNORE_TO, (myUI.textToFloat(myUI.viewEquipment_Set2_IGNORE_P.text())/100))
            SET_INFO['IGNORE_P'] = 0
            if (IGNORE_TO > myCharactor.getData()['IGNORE_P']):
                SET_INFO['IGNORE_P'] = 1 - ((1 - IGNORE_TO) / (1 - myCharactor.getData()['IGNORE_P']))
            if (IGNORE_TO < myCharactor.getData()['IGNORE_P']):
                SET_INFO['IGNORE_P'] = ((1 - myCharactor.getData()['IGNORE_P']) / (1 - IGNORE_TO)) - 1
            IMPROVE_INFO = myCharactor.calcImprove(SET_INFO)
            myUI.viewEquipment_Set2_IMPROVE.setText('增幅 ' + str(toPercentText(IMPROVE_INFO['TOTAL'])))


        except Exception as e:
            QtWidgets.QMessageBox.warning(me, '提示', '輸入資料有誤')
            print('calc_eq')
            print(e)
            pass

    # funtion: 計算等效無視
    def doCalcIgnore(me):
        try:
            myCharactor = me.myCharacter
            myUI = me.myUI

            IGNORE_BEFORE_TXT = myUI.viewTools_IGNORE_BEFORE.text()
            IGNORE_RANGE_TXT  = myUI.viewTools_IGNORE_RANGE.text()
            IGNORE_AFTER_TXT  = myUI.viewTools_IGNORE_AFTER.text()

            if (IGNORE_BEFORE_TXT == ''):
                QtWidgets.QMessageBox.warning(me, '提示', '請輸入原始無視')
                return False

            if (IGNORE_RANGE_TXT == '' and IGNORE_AFTER_TXT == ''):
                QtWidgets.QMessageBox.warning(me, '提示', '請輸入無視變量或結果無視')
                return False
            
            if (IGNORE_RANGE_TXT != ''):
                IGNORE_AFTER_TXT = ''

            if (IGNORE_RANGE_TXT != ''):
                IGNORE_AFTER_TXT = ''

            IGNORE_BEFORE = myUI.textToFloat(IGNORE_BEFORE_TXT) / 100
            IGNORE_RANGE  = myUI.textToFloat(IGNORE_RANGE_TXT) / 100
            IGNORE_AFTER  = myUI.textToFloat(IGNORE_AFTER_TXT) / 100

            if (IGNORE_BEFORE > 1 or IGNORE_RANGE > 1 or IGNORE_AFTER > 1):
                QtWidgets.QMessageBox.warning(me, '提示', '輸入資料有誤 無視防禦錯誤')
                return False

            if (IGNORE_AFTER_TXT == ''):
                IGNORE_AFTER = myCharactor.calcIgnore(IGNORE_BEFORE, IGNORE_RANGE)
                
                IGNORE_RANGE = round(IGNORE_RANGE * 100, 2)
                IGNORE_AFTER = round(IGNORE_AFTER * 100, 2)
                
                myUI.viewTools_IGNORE_RANGE.setText(str(IGNORE_RANGE))
                myUI.viewTools_IGNORE_AFTER.setText(str(IGNORE_AFTER))
                return True

            if (IGNORE_RANGE_TXT == ''):

                if (IGNORE_AFTER > IGNORE_BEFORE):
                    IGNORE_RANGE = 1 - (1 - IGNORE_AFTER) / (1 - IGNORE_BEFORE)
                if (IGNORE_AFTER < IGNORE_BEFORE):
                    IGNORE_RANGE = (1 - IGNORE_BEFORE) / (1 - IGNORE_AFTER) - 1

                IGNORE_RANGE = round(IGNORE_RANGE * 100, 2)
                IGNORE_AFTER = round(IGNORE_AFTER * 100, 2)

                myUI.viewTools_IGNORE_RANGE.setText(str(IGNORE_RANGE))
                myUI.viewTools_IGNORE_AFTER.setText(str(IGNORE_AFTER))
                return True
            
        except Exception as e:
            QtWidgets.QMessageBox.warning(me, '提示', '輸入資料有誤')
            print('doCalcIgnore')
            print(e)
            pass
# ------------------ APP 入口 ------------------
app = QtWidgets.QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())

