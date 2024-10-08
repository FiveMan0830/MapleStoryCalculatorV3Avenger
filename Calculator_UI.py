from PyQt5 import QtCore, QtWidgets, QtGui

class Calculator_UI():
    def setupUi(me, Form):
        me.version = '惡魔復仇者特別版'
        title = '裝備效益計算機 ' + me.version
        form_w = 600
        form_h = 527
        padding = 5
        Form.setWindowTitle(title)
        Form.resize(form_w, form_h)
        
        me.tabpanel = QtWidgets.QTabWidget(Form)
        me.tabpanel.setGeometry(QtCore.QRect(padding, padding, form_w-padding*2, form_h-padding*2))

        me.tabpanel.addTab(me.desingPage_Ability(), '能力值設定')
        me.tabpanel.addTab(me.desingPage_Parameter(), '角色參數')
        me.tabpanel.addTab(me.desingPage_Equipment(), '裝備變更')
        me.tabpanel.addTab(me.desingPage_Tools(), '工具')
        
        me.tabpanel.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # function: 能力值設定
    def desingPage_Ability(me):
        page = QtWidgets.QWidget()

        me.btnAbility_Submit = me.makeField(page, QtWidgets.QPushButton(page), 15, 270, 555, 30)
        me.btnAbility_Submit.setText('確定')
        
        me.btnAbility_SaveFile = me.makeField(page, QtWidgets.QPushButton(page), 300, 15, 270, 30)
        me.btnAbility_SaveFile.setText('儲存檔案')
        
        me.btnAbility_SelectFile = me.makeField(page, QtWidgets.QPushButton(page), 15, 15, 270, 30)
        me.btnAbility_SelectFile.setText('選擇檔案')
        
        me.viewAbility_LEVEL = me.makeField(page, QtWidgets.QLineEdit(page), 15, 60, 270, 24, '等級', 90)
        
        me.viewAbility_CLASS  = me.makeField(page, QtWidgets.QLineEdit(page), 300, 60, 270, 24, '職業', 90).setEnabled(False)

        me.viewAbility_ATTACK = me.makeField(page, QtWidgets.QLineEdit(page), 15, 90, 270, 24, '基礎攻擊', 90)
        me.viewAbility_DMG_P      = me.makeField(page, QtWidgets.QLineEdit(page), 15, 120, 270, 24, '傷害', 90, '％')
        me.viewAbility_FINALDMG_P = me.makeField(page, QtWidgets.QLineEdit(page), 15, 150, 270, 24, '最終傷害', 90, '％')
        me.viewAbility_BOSS_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 180, 270, 24, 'BOSS傷害', 90, '％')

        me.viewAbility_WP   = me.makeField(page, QtWidgets.QLineEdit(page), 300, 90 , 270, 24, '武器係數', 90).setEnabled(False)
        me.viewAbility_STRIKE_P = me.makeField(page, QtWidgets.QLineEdit(page), 300, 120, 270, 24, '爆擊傷害', 90, '％')
        me.viewAbility_ATTACK_P = me.makeField(page, QtWidgets.QLineEdit(page), 300, 150, 270, 24, '攻擊力％', 90, '％')
        me.viewAbility_IGNORE_P = me.makeField(page, QtWidgets.QLineEdit(page), 300, 180, 270, 24, '無視防禦', 90, '％')

        # 4大屬性
        me.viewAbility_HP_CLEAR = me.makeField(page, QtWidgets.QLineEdit(page), 15, 210, 200, 24, '吃% HP', 90)
        me.viewAbility_STR_CLEAR = me.makeField(page, QtWidgets.QLineEdit(page), 15, 240, 200, 24, '吃% STR', 90)

        me.viewAbility_HP_P = me.makeField(page, QtWidgets.QLineEdit(page), 230, 210, 125, 24, 'HP%', 55, '％')
        me.viewAbility_STR_P = me.makeField(page, QtWidgets.QLineEdit(page), 230, 240, 125, 24, 'STR%', 55, '％')

        me.viewAbility_HP_UNIQUE = me.makeField(page, QtWidgets.QLineEdit(page), 370, 210, 200, 24, '不吃% HP', 100)
        me.viewAbility_STR_UNIQUE = me.makeField(page, QtWidgets.QLineEdit(page), 370, 240, 200, 24, '不吃% STR', 100)

        me.viewAbility_DEFENSE_P = me.makeField(page, QtWidgets.QLineEdit(page), 15, 310, 270, 24, '怪物防禦', 90, '％')

        return page
    
    # function: 角色參數
    def desingPage_Parameter(me):
        page = QtWidgets.QWidget()

        # 等效增幅
        RANGE_TYPE = [
            '攻擊　 =', '％攻擊 =',
            '％總傷 =', '％Ｂ傷 =',
            '％爆傷 =', '％無視 =',
            '％全屬 =',
            'HP　 =', '%HP　 =', '不吃%HP　 =',
            '力量　 =', '％力量 =', '不吃％力 =',
        ]

        PARAMETER_TYPE = [
            'HP　', '%HP', '不吃%HP',
            '力量　', '％力量', '不吃％力',
            '％全屬',
            '攻擊　', '％攻擊',
            '％總傷', '％Ｂ傷',
            '％爆傷', '％無視',
        ]
        
        me.viewParameter_RANGE_VALUE = me.makeField(page, QtWidgets.QLineEdit(page), 10, 15, 35, 24)
        me.viewParameter_RANGE_VALUE.setText('1')

        me.viewParameter_RANGE_TYPE  = me.makeField(page, QtWidgets.QComboBox(page), 50, 15, 100, 24)
        me.viewParameter_RANGE_TYPE.addItems(RANGE_TYPE)

        me.makeField(page, QtWidgets.QLineEdit(page), 155, 15, 100, 24, '', 0, '％全屬', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 260, 15, 100, 24, '', 0, '　力量', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 365, 15, 100, 24, '', 0, '％力量', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 470, 15, 100, 24, '', 0, '不吃％力', 50).setEnabled(False)
        
        me.makeField(page, QtWidgets.QLineEdit(page), 50, 45, 100, 24, '', 0, '　攻擊', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 155, 45, 100, 24, '', 0, '％攻擊', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 260, 45, 100, 24, '', 0, '　HP', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 365, 45, 100, 24, '', 0, '％HP', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 470, 45, 100, 24, '', 0, '不吃％HP', 50).setEnabled(False)
        
        me.makeField(page, QtWidgets.QLineEdit(page), 50, 75, 100, 24, '', 0, '％總傷', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 155, 75, 100, 24, '', 0, '％BOSS', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 260, 75, 100, 24, '', 0, '％爆傷', 50).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 365, 75, 100, 24, '', 0, '％無視', 50).setEnabled(False)

        me.viewParameter_EQUIVALENT_ALL_P       = me.makeField(page, QtWidgets.QLabel(page), 5 + 155, 15, 100, 24)
        me.viewParameter_EQUIVALENT_STR_CLEAR   = me.makeField(page, QtWidgets.QLabel(page), 5 + 260, 15, 100, 24)
        me.viewParameter_EQUIVALENT_STR_P       = me.makeField(page, QtWidgets.QLabel(page), 5 + 365, 15, 100, 24)
        me.viewParameter_EQUIVALENT_STR_UNIQUE  = me.makeField(page, QtWidgets.QLabel(page), 5 + 470, 15, 100, 24)
        
        me.viewParameter_EQUIVALENT_Att         = me.makeField(page, QtWidgets.QLabel(page), 5 + 50 , 45, 100, 24)
        me.viewParameter_EQUIVALENT_Att_P       = me.makeField(page, QtWidgets.QLabel(page), 5 + 155, 45, 100, 24)
        me.viewParameter_EQUIVALENT_HP_CLEAR    = me.makeField(page, QtWidgets.QLabel(page), 5 + 260,  45, 100, 24)
        me.viewParameter_EQUIVALENT_HP_P        = me.makeField(page, QtWidgets.QLabel(page), 5 + 365,  45, 100, 24)
        me.viewParameter_EQUIVALENT_HP_UNIQUE   = me.makeField(page, QtWidgets.QLabel(page), 5 + 470,  45, 100, 24)

        me.viewParameter_EQUIVALENT_Dmg_P       = me.makeField(page, QtWidgets.QLabel(page), 5 + 50 , 75, 100, 24)
        me.viewParameter_EQUIVALENT_Boss_P      = me.makeField(page, QtWidgets.QLabel(page), 5 + 155, 75, 100, 24)
        
        me.viewParameter_EQUIVALENT_Strike_P    = me.makeField(page, QtWidgets.QLabel(page), 5 + 260 , 75, 100, 24)
        me.viewParameter_EQUIVALENT_Ignore_P    = me.makeField(page, QtWidgets.QLabel(page), 5 + 365, 75, 100, 24)
        
        # 單項增幅
        me.viewParameter_IMPROVE_VALUE_STR_CLEAR    = me.makeField(page, QtWidgets.QLineEdit(page), 15, 140, 115, 24, '力量　 增加', 65)
        me.viewParameter_IMPROVE_VALUE_STR_P        = me.makeField(page, QtWidgets.QLineEdit(page), 15, 170, 115, 24, '力量％　 增加', 65, '%')
        me.viewParameter_IMPROVE_VALUE_STR_UNIQUE   = me.makeField(page, QtWidgets.QLineEdit(page), 15, 200, 115, 24, '不吃％力 增加', 65)
        me.viewParameter_IMPROVE_VALUE_HP_CLEAR    = me.makeField(page, QtWidgets.QLineEdit(page), 15, 230, 115, 24, 'HP　 增加', 65)
        me.viewParameter_IMPROVE_VALUE_HP_P        = me.makeField(page, QtWidgets.QLineEdit(page), 15, 260, 115, 24, 'HP％ 增加', 65, '%')
        me.viewParameter_IMPROVE_VALUE_HP_UNIQUE   = me.makeField(page, QtWidgets.QLineEdit(page), 15, 290, 115, 24, '不吃％HP 增加', 65)
        me.viewParameter_IMPROVE_VALUE_ALL_P        = me.makeField(page, QtWidgets.QLineEdit(page), 15, 320, 115, 24, '全屬％ 增加', 65, '%')

        me.viewParameter_IMPROVE_VALUE_DMG_P    = me.makeField(page, QtWidgets.QLineEdit(page), 15, 350, 115, 24, '總傷％ 增加', 65, '%')
        me.viewParameter_IMPROVE_VALUE_BOSS_P   = me.makeField(page, QtWidgets.QLineEdit(page), 15, 380, 115, 24, 'Ｂ傷％ 增加', 65, '%')
        me.viewParameter_IMPROVE_VALUE_STRIKE_P = me.makeField(page, QtWidgets.QLineEdit(page), 15, 410, 115, 24, '爆傷％ 增加', 65, '%')
        me.viewParameter_IMPROVE_VALUE_IGNORE_P = me.makeField(page, QtWidgets.QLineEdit(page), 15, 440, 115, 24, '無視％ 增加', 65, '%')
        me.viewParameter_IMPROVE_VALUE_ATT      = me.makeField(page, QtWidgets.QLineEdit(page), 240, 140, 115, 24, '攻擊　 增加', 65)
        me.viewParameter_IMPROVE_VALUE_ATT_P    = me.makeField(page, QtWidgets.QLineEdit(page), 240, 170, 115, 24, '攻擊％ 增加', 65, '%')

        me.viewParameter_IMPROVE_STR_CLEAR  = me.makeField(page, QtWidgets.QLabel(page), 140, 140, 120, 24)
        me.viewParameter_IMPROVE_STR_P      = me.makeField(page, QtWidgets.QLabel(page), 140, 170, 120, 24)
        me.viewParameter_IMPROVE_STR_UNIQUE = me.makeField(page, QtWidgets.QLabel(page), 140, 200, 120, 24)
        me.viewParameter_IMPROVE_HP_CLEAR  = me.makeField(page, QtWidgets.QLabel(page), 140, 230, 120, 24)
        me.viewParameter_IMPROVE_HP_P      = me.makeField(page, QtWidgets.QLabel(page), 140, 260, 120, 24)
        me.viewParameter_IMPROVE_HP_UNIQUE = me.makeField(page, QtWidgets.QLabel(page), 140, 290, 120, 24)
        me.viewParameter_IMPROVE_ALL_P      = me.makeField(page, QtWidgets.QLabel(page), 140, 320, 120, 24)

        me.viewParameter_IMPROVE_ATT      = me.makeField(page, QtWidgets.QLabel(page), 360, 140, 120, 24)
        me.viewParameter_IMPROVE_ATT_P    = me.makeField(page, QtWidgets.QLabel(page), 360, 170, 120, 24)
        me.viewParameter_IMPROVE_DMG_P    = me.makeField(page, QtWidgets.QLabel(page), 140, 350, 120, 24)
        me.viewParameter_IMPROVE_BOSS_P   = me.makeField(page, QtWidgets.QLabel(page), 140, 380, 120, 24)
        me.viewParameter_IMPROVE_STRIKE_P = me.makeField(page, QtWidgets.QLabel(page), 140, 410, 120, 24)
        me.viewParameter_IMPROVE_IGNORE_P = me.makeField(page, QtWidgets.QLabel(page), 140, 440, 120, 24)

        impTxt = '增幅 0.0%'
        me.viewParameter_IMPROVE_STR_CLEAR.setText(impTxt)
        me.viewParameter_IMPROVE_STR_P.setText(impTxt)
        me.viewParameter_IMPROVE_STR_UNIQUE.setText(impTxt)
        me.viewParameter_IMPROVE_HP_CLEAR.setText(impTxt)
        me.viewParameter_IMPROVE_HP_P.setText(impTxt)
        me.viewParameter_IMPROVE_HP_UNIQUE.setText(impTxt)
        me.viewParameter_IMPROVE_ALL_P.setText(impTxt)

        me.viewParameter_IMPROVE_ATT.setText(impTxt)
        me.viewParameter_IMPROVE_ATT_P.setText(impTxt)
        me.viewParameter_IMPROVE_DMG_P.setText(impTxt)
        me.viewParameter_IMPROVE_BOSS_P.setText(impTxt)
        me.viewParameter_IMPROVE_STRIKE_P.setText(impTxt)
        me.viewParameter_IMPROVE_IGNORE_P.setText(impTxt)

        me.viewParameter_IMPROVE_Total = me.makeField(page, QtWidgets.QLabel(page), 240, 200, 400, 24)
        me.viewParameter_IMPROVE_Total.setText('總增幅 0.000%')

        me.viewParameter_IMPROVE_VALUE_AS = me.makeField(page, QtWidgets.QLabel(page), 240, 230, 150, 24)
        me.viewParameter_IMPROVE_VALUE_AS.setText('等同於 增加 0.00')
        
        me.viewParameter_IMPROVE_VALUE_AS_PARAMETER = me.makeField(page, QtWidgets.QComboBox(page), 240, 260, 110, 24)
        me.viewParameter_IMPROVE_VALUE_AS_PARAMETER.addItems(PARAMETER_TYPE)

        # 推估數值
        me.makeField(page, QtWidgets.QLineEdit(page), 460, 140 + 36 * 0, 110, 36).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 460, 140 + 36 * 1, 110, 36).setEnabled(False)
        me.makeField(page, QtWidgets.QLineEdit(page), 460, 153 + 36 * 4, 110,107).setEnabled(False)

        me.viewParameter_ESTIMATE_STR   = me.makeField(page, QtWidgets.QLabel(page), 462, 140 + 18 * 0, 108, 18, 'STR' , 40, '' , 19)
        me.viewParameter_ESTIMATE_STR_P = me.makeField(page, QtWidgets.QLabel(page), 462, 140 + 18 * 1, 108, 18, 'STR%', 40, '%', 19)

        me.viewParameter_ESTIMATE_HP   = me.makeField(page, QtWidgets.QLabel(page), 462, 140 + 18 * 2, 108, 18, 'HP' , 40, '' , 19)
        me.viewParameter_ESTIMATE_HP_P = me.makeField(page, QtWidgets.QLabel(page), 462, 140 + 18 * 3, 108, 18, 'HP%', 40, '%', 19)

        me.viewParameter_ESTIMATE_ATTACK   = me.makeField(page, QtWidgets.QLabel(page), 462, 153 + 18 * 8, 108, 18, '攻擊' , 40, '' , 19)
        me.viewParameter_ESTIMATE_ATTACK_P = me.makeField(page, QtWidgets.QLabel(page), 462, 153 + 18 * 9, 108, 18, '攻擊%', 40, '%', 19)
        me.viewParameter_ESTIMATE_DMG_P    = me.makeField(page, QtWidgets.QLabel(page), 462, 153 + 18 *10, 108, 18, '傷害%', 40, '%', 19)
        me.viewParameter_ESTIMATE_BOSS_P   = me.makeField(page, QtWidgets.QLabel(page), 462, 153 + 18 *11, 108, 18, 'Ｂ傷%', 40, '%', 19)
        me.viewParameter_ESTIMATE_STRIKE_P = me.makeField(page, QtWidgets.QLabel(page), 462, 153 + 18 *12, 108, 18, '爆傷%', 40, '%', 19)
        me.viewParameter_ESTIMATE_IGNORE_P = me.makeField(page, QtWidgets.QLabel(page), 462, 153 + 18 *13, 108, 18, '無視%', 40, '%', 19)
        
        return page
    
    # function: 裝備變更
    def desingPage_Equipment(me):
        page = QtWidgets.QWidget()

        
        me.makeField(page, QtWidgets.QLabel(page), 15, 15, 130, 24).setText('原裝備能力')
        me.makeField(page, QtWidgets.QLineEdit(page), 11, 38, 138, 268).setEnabled(False)
        me.viewEquipment_origin_STR       = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  1, 130, 24, 'STR' , 55, '')
        me.viewEquipment_origin_STR_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  2, 130, 24, 'STR%', 55, '％')
        me.viewEquipment_origin_HP       = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  3, 130, 24, 'HP' , 55, '')
        me.viewEquipment_origin_HP_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  4, 130, 24, 'HP%', 55, '％')
        # me.viewEquipment_origin_DEX       = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  3, 130, 24, 'DEX' , 55, '')
        # me.viewEquipment_origin_DEX_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  4, 130, 24, 'DEX%', 55, '％')
        # me.viewEquipment_origin_INT       = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  5, 130, 24, 'INT' , 55, '')
        # me.viewEquipment_origin_INT_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  6, 130, 24, 'INT%', 55, '％')
        # me.viewEquipment_origin_LUK       = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  7, 130, 24, 'LUK' , 55, '')
        # me.viewEquipment_origin_LUK_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  8, 130, 24, 'LUK%', 55, '％')
        me.viewEquipment_origin_ALL_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  5, 130, 24, '全屬%', 55, '％')
        me.viewEquipment_origin_ATTACK    = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  6, 130, 24, '攻擊' , 55, '')
        me.viewEquipment_origin_ATTACK_P  = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  7, 130, 24, '攻擊%', 55, '％')
        me.viewEquipment_origin_DMG_P     = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  8, 130, 24, '傷害%', 55, '％')
        me.viewEquipment_origin_STRIKE_P  = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 *  9, 130, 24, '爆傷%', 55, '％')
        me.viewEquipment_origin_IGNORE_P  = me.makeField(page, QtWidgets.QLineEdit(page), 15, 15 + 26 * 10, 130, 24, '無視%', 55, '％')
        # me.viewEquipment_origin_IMPROVE   = me.makeField(page, QtWidgets.QLabel(page), 15, 15 + 26 * 15, 130, 24)
        # me.viewEquipment_origin_IMPROVE.setText('增幅 0.0%')

        me.makeField(page, QtWidgets.QLabel(page), 192, 15, 130, 24).setText('更換裝備1')
        me.makeField(page, QtWidgets.QLineEdit(page), 188, 38, 138, 268).setEnabled(False)
        me.viewEquipment_Set1_STR       = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  1, 130, 24, 'STR' , 55, '')
        me.viewEquipment_Set1_STR_P     = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  2, 130, 24, 'STR%', 55, '％')
        me.viewEquipment_Set1_HP       = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  3, 130, 24, 'HP' , 55, '')
        me.viewEquipment_Set1_HP_P     = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  4, 130, 24, 'HP%', 55, '％')
        # me.viewEquipment_Set1_DEX       = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  3, 130, 24, 'DEX' , 55, '')
        # me.viewEquipment_Set1_DEX_P     = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  4, 130, 24, 'DEX%', 55, '％')
        # me.viewEquipment_Set1_INT       = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  5, 130, 24, 'INT' , 55, '')
        # me.viewEquipment_Set1_INT_P     = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  6, 130, 24, 'INT%', 55, '％')
        # me.viewEquipment_Set1_LUK       = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  7, 130, 24, 'LUK' , 55, '')
        # me.viewEquipment_Set1_LUK_P     = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  8, 130, 24, 'LUK%', 55, '％')
        me.viewEquipment_Set1_ALL_P     = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  5, 130, 24, '全屬%', 55, '％')
        me.viewEquipment_Set1_ATTACK    = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  6, 130, 24, '攻擊' , 55, '')
        me.viewEquipment_Set1_ATTACK_P  = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  7, 130, 24, '攻擊%', 55, '％')
        me.viewEquipment_Set1_DMG_P     = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  8, 130, 24, '傷害%', 55, '％')
        me.viewEquipment_Set1_STRIKE_P  = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 *  9, 130, 24, '爆傷%', 55, '％')
        me.viewEquipment_Set1_IGNORE_P  = me.makeField(page, QtWidgets.QLineEdit(page), 192, 15 + 26 * 10, 130, 24, '無視%', 55, '％')
        me.viewEquipment_Set1_IMPROVE   = me.makeField(page, QtWidgets.QLabel(page),    192, 15 + 26 * 11, 130, 24)
        me.viewEquipment_Set1_IMPROVE.setText('增幅 0.0%')

        me.makeField(page, QtWidgets.QLabel(page), 370, 15, 130, 24).setText('更換裝備2')
        me.makeField(page, QtWidgets.QLineEdit(page), 366, 38, 138, 268).setEnabled(False)
        me.viewEquipment_Set2_STR       = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  1, 130, 24, 'STR' , 55, '')
        me.viewEquipment_Set2_STR_P     = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  2, 130, 24, 'STR%', 55, '％')
        me.viewEquipment_Set2_HP       = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  3, 130, 24, 'HP' , 55, '')
        me.viewEquipment_Set2_HP_P     = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  4, 130, 24, 'HP%', 55, '％')
        # me.viewEquipment_Set2_DEX       = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  3, 130, 24, 'DEX' , 55, '')
        # me.viewEquipment_Set2_DEX_P     = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  4, 130, 24, 'DEX%', 55, '％')
        # me.viewEquipment_Set2_INT       = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  5, 130, 24, 'INT' , 55, '')
        # me.viewEquipment_Set2_INT_P     = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  6, 130, 24, 'INT%', 55, '％')
        # me.viewEquipment_Set2_LUK       = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  7, 130, 24, 'LUK' , 55, '')
        # me.viewEquipment_Set2_LUK_P     = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  8, 130, 24, 'LUK%', 55, '％')
        me.viewEquipment_Set2_ALL_P     = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  5, 130, 24, '全屬%', 55, '％')
        me.viewEquipment_Set2_ATTACK    = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  6, 130, 24, '攻擊' , 55, '')
        me.viewEquipment_Set2_ATTACK_P  = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  7, 130, 24, '攻擊%', 55, '％')
        me.viewEquipment_Set2_DMG_P     = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  8, 130, 24, '傷害%', 55, '％')
        me.viewEquipment_Set2_STRIKE_P  = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 *  9, 130, 24, '爆傷%', 55, '％')
        me.viewEquipment_Set2_IGNORE_P  = me.makeField(page, QtWidgets.QLineEdit(page), 370, 15 + 26 * 10, 130, 24, '無視%', 55, '％')
        me.viewEquipment_Set2_IMPROVE   = me.makeField(page, QtWidgets.QLabel(page),    370, 15 + 26 * 11, 130, 24)
        me.viewEquipment_Set2_IMPROVE.setText('增幅 0.0%')

        # me.viewEquipment_Set1_IGNORE_P.setEnabled(False)
        # me.viewEquipment_Set2_IGNORE_P.setEnabled(False)
        
        return page
    
    # function: 工具
    def desingPage_Tools(me):
        page = QtWidgets.QWidget()
        
        me.viewTools_IGNORE_BEFORE = me.makeField(page, QtWidgets.QLineEdit(page),  15, 15, 150, 24, '無視防禦', 75, '%')
        me.viewTools_IGNORE_RANGE  = me.makeField(page, QtWidgets.QLineEdit(page), 170, 15, 95, 24, ' + ', 20, '%')
        me.viewTools_IGNORE_AFTER  = me.makeField(page, QtWidgets.QLineEdit(page), 270, 15, 95, 24, ' = ', 20, '%')
        me.btnTools_IGNORE_SUBMIT  = me.makeField(page, QtWidgets.QPushButton(page), 365, 15, 65, 24)
        me.btnTools_IGNORE_SUBMIT.setText('計算')

        return page

    # function: 使用說明
    def desingPage_Memo(me):
        page = QtWidgets.QWidget()
        
        me.makeField(page, QtWidgets.QLabel(page), 15, 400, 800, 24,).setText('原作者：牡羊  修改者：環櫻\t版本號碼：' + me.version)
        
        me.makeField(page, QtWidgets.QLabel(page), 15, 15 + 30 * 0, 800, 24,).setText('1. 所有能力值皆須填寫BUFF後的狀態')
        me.makeField(page, QtWidgets.QLabel(page), 15, 15 + 30 * 1, 800, 24,).setText('2. 能力值設定填寫時，吃％屬性即面板上的\"基本數值\"')
        me.makeField(page, QtWidgets.QLabel(page), 15, 15 + 30 * 2, 800, 24,).setText('3. 此計算機提供數值僅為參考用，若因此工具衍伸的問題將不負責任')
        me.makeField(page, QtWidgets.QLabel(page), 15, 15 + 30 * 3, 800, 24,).setText('4. 如有使用問題請到巴哈「新楓之谷」版搜尋「裝備效益計算機」回報')
        
        return page
    
    # function: 產生輸入框
    def makeField(me, page, obj, x, y, width, height, prefixText = '', labelWidth = 0, subfixText = '', subLabelWidth = 0):
        # 前綴文字
        if (prefixText != ''):
            if (labelWidth == 0): labelWidth = 55
            label = QtWidgets.QLabel(page)
            label.setText(prefixText)
            label.setGeometry(QtCore.QRect(x, y, labelWidth, height))

        obj.setGeometry(QtCore.QRect(x + labelWidth, y, width - labelWidth, height))
        
        # 後綴文字
        if (subfixText != ''):
            if (subLabelWidth == 0): subLabelWidth = 20
            sublabel = QtWidgets.QLabel(page)
            sublabel.setText(subfixText)
            sublabel.setGeometry(QtCore.QRect(x + width - subLabelWidth + 5, y, subLabelWidth - 5, height))
            sublabel.setEnabled(False)
        return obj
    
    # function: 將字串轉換為 float
    def textToFloat(me, text):
        value = 0
        if(text == '-'): text = ''
        if(text != ''): value = float(text)
        return value

    # function: 將字串轉換為 float
    def textToInt(me, text):
        value = 0
        if(text == '-'): text = ''
        if(text != ''): value = int(text)
        return value

    def getColor(me, value):
        return 'color: ' + str(value >= 1 and (value == 1 and 'black' or 'red') or 'blue')
    
    
    

