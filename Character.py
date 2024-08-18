class Character():
    def __init__(me):
        me.isReset = False
        me.reset()

    # 職業
    def getClass(me):
        return '惡魔復仇者'
    
    # 武器係數
    def getWeaponParam(me):
        return 1.3

    # Object: 取得職業對應參數
    def getInfo(me):
        CLASS_INFO = {
            'WP_VALUE': 1.3,
            'LEVEL': 1,
            'HP': '',
            'STR': '',
            'DEX': '',
            'INT': '',
            'LUK': '',
        }

        return CLASS_INFO

    # Object: 取得角色資料 me.data
    def getData(me):
        return me.data
    
    # function: 初始化角色資料 me.data
    def reset(me):
        me.data = {
            'LEVEL': 0,
            'CLASS_IDX': 0, 'CLASS_NAME': '惡魔復仇者',
            'WP_IDX': 0, 'WP_VALUE': 1.3,
            'ATTACK': 0, 'ATTACK_P': 0,
            'DMG_P': 0, 'BOSS_P': 0,
            'STRIKE_P': 0,
            'IGNORE_P': 0,
            'FINALDMG_P': 0,
            'DEFENSE_P': 0,

            'HP': 0, 
            'HP_P': 0, 'HP_CLEAR': 0, 'HP_UNIQUE': 0,

            'STR': 0, 
            'STR_P': 0, 'STR_CLEAR': 0, 'STR_UNIQUE': 0,

            'FIX': 1
        }
        me.isReset = True

    # function: 更新角色能力值到 me.data
    def updateAbilityByData(me, data):

        if('LEVEL' in data): me.data['LEVEL'] = data['LEVEL']
        if('ATTACK' in data): me.data['ATTACK'] = data['ATTACK']
        if('ATTACK_P' in data): me.data['ATTACK_P'] = data['ATTACK_P']
        if('DMG_P' in data): me.data['DMG_P'] = data['DMG_P']
        if('BOSS_P' in data): me.data['BOSS_P'] = data['BOSS_P']
        if('STRIKE_P' in data): me.data['STRIKE_P'] = data['STRIKE_P']
        if('IGNORE_P' in data): me.data['IGNORE_P'] = data['IGNORE_P']
        if('FINALDMG_P' in data): me.data['FINALDMG_P'] = data['FINALDMG_P']
        if('DEFENSE_P' in data): me.data['DEFENSE_P'] = data['DEFENSE_P']

        if('HP_CLEAR' in data): me.data['HP_CLEAR'] = data['HP_CLEAR']
        if('HP_P' in data): me.data['HP_P'] = data['HP_P']
        if('HP_UNIQUE' in data): me.data['HP_UNIQUE'] = data['HP_UNIQUE']

        if('STR_CLEAR' in data): me.data['STR_CLEAR'] = data['STR_CLEAR']
        if('STR_P' in data): me.data['STR_P'] = data['STR_P']
        if('STR_UNIQUE' in data): me.data['STR_UNIQUE'] = data['STR_UNIQUE']

        # 計算HP
        me.data['HP'] = data['HP_CLEAR'] * (1 + data['HP_P']) + data['HP_UNIQUE']
        me.data['STR'] = data['STR_CLEAR'] * (1 + data['STR_P']) + data['STR_UNIQUE']
        

        """
        # print(CLASS_NAME)
        myAttribute = me.calcAttributeByClass(me.data)
        WP_VALUE = me.data['WP_VALUE']
        ATTACK_P = me.data['ATTACK_P']
        DMG_P = me.data['DMG_P']
        FINALDMG_P = me.data['FINALDMG_P']
        

        ATTACK = 1#MAX_DMG / ( myAttribute * WP_VALUE * (1 + ATTACK_P) * 0.01 * (1 + DMG_P) * (1 + FINALDMG_P) )
        if(me.data['ATTACK'] == 0):
            me.data['ATTACK'] = ATTACK
        else:
            me.data['FIX'] = ATTACK / me.data['ATTACK']
        """
        print('\n------------ updateAbilityByData ------------')
        print(me.data)
        me.isReset = False
        return me.data
    
    # 屬性參數  公式 = (AP血量/3.5) + (總血量-AP血量) / 3.5 * 0.8 + 力量
    def calcAttrParam(me, data):
        characterAttrParam = (data['HP_BASE']/3.5) + (data['HP'] - data['HP_BASE']) / 3.5 * 0.8 + data['STR']
        return characterAttrParam
    
    # function: 計算推估無視
    def calcIgnore(me, origin, range):
        IGNORE_P = origin
        if (range > 0):
            IGNORE_P = 1 - ((1 - IGNORE_P) * (1 - range))
        if (range < 0):
            IGNORE_P = 1 - ((1 - IGNORE_P) / (1 + range))
        if (IGNORE_P > 1): IGNORE_P = 1
        return IGNORE_P
    
    # function: 取得預估值
    def getEstimate(me, new_data):
        data = me.getData()
        ESTIMATE_INFO = {
            'DMG_P': data['DMG_P'],
            'STRIKE_P': data['STRIKE_P'],
            'FINALDMG_P': data['FINALDMG_P'],
            'ATTACK': data['ATTACK'],
            'ATTACK_P': data['ATTACK_P'],
            'BOSS_P': data['BOSS_P'],
            'IGNORE_P': data['IGNORE_P'],

            'STR_CLEAR': data['STR_CLEAR'],
            'STR_P': data['STR_P'],
            'STR_UNIQUE': data['STR_UNIQUE'],
            'STR': 0,

            'HP_CLEAR': data['HP_CLEAR'],
            'HP_P': data['HP_P'],
            'HP_UNIQUE': data['HP_UNIQUE'],
            'HP': 0,

            'ALL_P': 0,
        }
        
        # 傷害
        if('DMG_P' in new_data):
            ESTIMATE_INFO['DMG_P'] += new_data['DMG_P']

        # BOSS
        if('BOSS_P' in new_data):
            ESTIMATE_INFO['BOSS_P'] += new_data['BOSS_P']

        # 攻擊力
        if('ATTACK' in new_data):
            ESTIMATE_INFO['ATTACK'] += new_data['ATTACK']

        # 攻擊%
        if('ATTACK_P' in new_data):
            ESTIMATE_INFO['ATTACK_P'] += new_data['ATTACK_P']
        
        # 爆傷
        if('STRIKE_P' in new_data):
            ESTIMATE_INFO['STRIKE_P'] += new_data['STRIKE_P']

        # 無視
        if('IGNORE_P' in new_data):
            ESTIMATE_INFO['IGNORE_P'] = me.calcIgnore(data['IGNORE_P'], new_data['IGNORE_P'])

        # 終傷
        if('FINALDMG_P' in new_data):
            ESTIMATE_INFO['FINALDMG_P'] += new_data['FINALDMG_P']

        # HP_CLEAR
        if('HP_CLEAR' in new_data):
            ESTIMATE_INFO['HP_CLEAR'] += new_data['HP_CLEAR']

        # HP_P
        if('HP_P' in new_data):
            ESTIMATE_INFO['HP_P'] += new_data['HP_P']

        # HP_UNIQUE
        if('HP_UNIQUE' in new_data):
            ESTIMATE_INFO['HP_UNIQUE'] += new_data['HP_UNIQUE']

        # STR_CLEAR
        if('STR_CLEAR' in new_data):
            ESTIMATE_INFO['STR_CLEAR'] += new_data['STR_CLEAR']

        # STR_P
        if('STR_P' in new_data):
            ESTIMATE_INFO['STR_P'] += new_data['STR_P']

        # STR_UNIQUE
        if('STR_UNIQUE' in new_data):
            ESTIMATE_INFO['STR_UNIQUE'] += new_data['STR_UNIQUE']

        # ALL_P
        if('ALL_P' in new_data):
            ESTIMATE_INFO['ALL_P'] += new_data['ALL_P']

        ESTIMATE_INFO['STR'] = ESTIMATE_INFO['STR_CLEAR'] * (1 + ESTIMATE_INFO['STR_P'] + ESTIMATE_INFO['ALL_P']) + ESTIMATE_INFO['STR_UNIQUE']
        ESTIMATE_INFO['HP'] = ESTIMATE_INFO['HP_CLEAR'] * (1 + ESTIMATE_INFO['HP_P']) + ESTIMATE_INFO['HP_UNIQUE']
        
        return ESTIMATE_INFO

    # function: 計算增幅
    def calcImprove(me, new_data):
        data = me.getData()
        IMPROVE_INFO = {
            'DMG_P': 1,
            'STRIKE_P': 1,
            'FINALDMG_P': 1,
            'ATTACK': 1,
            'ATTACK_P': 1,
            'BOSS_P': 1,
            'IGNORE_P': 1,

            'STR_CLEAR': 1,
            'STR_P': 1,
            'STR_UNIQUE': 1,

            'HP_CLEAR': 1,
            'HP_P': 1,
            'HP_UNIQUE': 1,

            'ALL_P': 1,
            'TOTAL': 1
        }

        ESTIMATE_INFO = me.getEstimate(new_data)

        
        # 傷害
        IMPROVE_INFO['DMG_P'] = (1 + ESTIMATE_INFO['DMG_P'] + data['BOSS_P']) / (1 + data['DMG_P'] + data['BOSS_P'])

        # BOSS
        IMPROVE_INFO['BOSS_P'] = (1 + data['DMG_P'] + ESTIMATE_INFO['BOSS_P']) / (1 + data['DMG_P'] + data['BOSS_P'])

        # 攻擊力
        IMPROVE_INFO['ATTACK'] = (ESTIMATE_INFO['ATTACK']) / data['ATTACK']
            

        # 攻擊%
        IMPROVE_INFO['ATTACK_P'] = (1 + ESTIMATE_INFO['ATTACK_P']) / (1 + data['ATTACK_P'])    
        
        # 爆傷
        IMPROVE_INFO['STRIKE_P'] = (1.35 + ESTIMATE_INFO['STRIKE_P']) / (1.35 + data['STRIKE_P'])    

        # 無視
        IMPROVE_INFO['IGNORE_P'] = (1 - (data['DEFENSE_P'] * (1 - ESTIMATE_INFO['IGNORE_P']))) / (1 - (data['DEFENSE_P'] * (1 - data['IGNORE_P'])))    
            

        # 終傷
        IMPROVE_INFO['FINALDMG_P'] = (1 + ESTIMATE_INFO['FINALDMG_P']) / (1 + data['FINALDMG_P'])

        

        # 取得原數值
        def getOrigin():
            ORIGIN_ATTRIBUTE = {
                'LEVEL': data['LEVEL'],
                'HP_BASE': (data['LEVEL'] * 90) + 545,
                'HP': data['HP'],
                'STR': data['STR'],
            }
            return ORIGIN_ATTRIBUTE
        
        myAttribute = me.calcAttrParam(getOrigin())


        # STR 增幅
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['STR'] = (ESTIMATE_INFO['STR_CLEAR'] * (1 + data['STR_P'])) + data['STR_UNIQUE']
        IMPROVE_INFO['STR_CLEAR'] = me.calcAttrParam(NEW_ATTRIBUTE) / myAttribute

        # 力量% 增幅
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['STR'] = (data['STR_CLEAR'] * (1 + ESTIMATE_INFO['STR_P'])) + data['STR_UNIQUE']
        IMPROVE_INFO['STR_P'] = me.calcAttrParam(NEW_ATTRIBUTE) / myAttribute
        
        # 不吃%力量 增幅
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['STR'] = (data['STR_CLEAR'] * (1 + data['STR_P'])) + ESTIMATE_INFO['STR_UNIQUE']
        IMPROVE_INFO['STR_UNIQUE'] = me.calcAttrParam(NEW_ATTRIBUTE) / myAttribute

        

        # HP 增幅
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['HP'] = (ESTIMATE_INFO['HP_CLEAR'] * (1 + data['HP_P'])) + data['HP_UNIQUE']
        IMPROVE_INFO['HP_CLEAR'] = me.calcAttrParam(NEW_ATTRIBUTE) / myAttribute


        # HP% 增幅
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['HP'] = (data['HP_CLEAR'] * (1 + ESTIMATE_INFO['HP_P'])) + data['HP_UNIQUE']
        IMPROVE_INFO['HP_P'] = me.calcAttrParam(NEW_ATTRIBUTE) / myAttribute
        
        # 不吃%HP 增幅
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['HP'] = (data['HP_CLEAR'] * (1 + data['HP_P'])) + ESTIMATE_INFO['HP_UNIQUE']
        IMPROVE_INFO['HP_UNIQUE'] = me.calcAttrParam(NEW_ATTRIBUTE) / myAttribute

        # 全屬% 增幅
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['STR'] = (data['STR_CLEAR'] * (1 + data['STR_P'] + ESTIMATE_INFO['ALL_P'])) + data['STR_UNIQUE']
        IMPROVE_INFO['ALL_P'] = me.calcAttrParam(NEW_ATTRIBUTE) / myAttribute
        
        # 計算總增幅
        IMPROVE_INFO['TOTAL'] = IMPROVE_INFO['STRIKE_P'] * IMPROVE_INFO['FINALDMG_P'] * IMPROVE_INFO['ATTACK'] * IMPROVE_INFO['ATTACK_P'] * IMPROVE_INFO['IGNORE_P']
        
        # 重算: (傷害+BOSS)增幅
        FINAL_IMPROVE_DMG = (1 + ESTIMATE_INFO['DMG_P'] + ESTIMATE_INFO['BOSS_P']) / (1 + data['DMG_P'] + data['BOSS_P'])
        IMPROVE_INFO['TOTAL'] = IMPROVE_INFO['TOTAL'] * FINAL_IMPROVE_DMG

        # 重算: 屬性增幅
        NEW_ATTRIBUTE = getOrigin()
        NEW_ATTRIBUTE['HP'] = ESTIMATE_INFO['HP']
        NEW_ATTRIBUTE['STR'] = ESTIMATE_INFO['STR']
        FINAL_IMPROVE_ATTRIBUTE = me.calcAttrParam(NEW_ATTRIBUTE) / myAttribute
        
        IMPROVE_INFO['TOTAL'] = IMPROVE_INFO['TOTAL'] * FINAL_IMPROVE_ATTRIBUTE
        
        return IMPROVE_INFO

    # function: 計算等效需求
    def getEquivalent(me, range):
        data = me.data

        IMPROVE_RANGE = range

        STATE_INFO = {
            'ATTACK': 0,
            'ATTACK_P': 0,
            'DMG_P': 0,
            'BOSS_P': 0,
            'STRIKE_P': 0,
            'IGNORE_P': 0,
            
            'ALL_P': 0,

            'HP_CLEAR': 0,
            'HP_P': 0,
            'HP_UNIQUE': 0,
            
            'STR_CLEAR': 0,
            'STR_P': 0,
            'STR_UNIQUE': 0,
        }

        if (IMPROVE_RANGE == 1):
            return STATE_INFO

        STATE_INFO['ATTACK'] = data['ATTACK'] * (IMPROVE_RANGE - 1)
        STATE_INFO['ATTACK_P'] = (1 + data['ATTACK_P']) * (IMPROVE_RANGE - 1)
        STATE_INFO['DMG_P'] = (1 + data['DMG_P'] + data['BOSS_P']) * (IMPROVE_RANGE - 1)
        STATE_INFO['BOSS_P'] = (1 + data['DMG_P'] + data['BOSS_P']) * (IMPROVE_RANGE - 1)
        STATE_INFO['STRIKE_P'] = (1.35 + data['STRIKE_P']) * (IMPROVE_RANGE - 1)

        # 計算無視效益
        defense = data['DEFENSE_P']
        FINAL_DMG = (1 - (defense * (1 - data['IGNORE_P']))) * IMPROVE_RANGE
        NEW_IGNORE = (defense - (1 - FINAL_DMG)) / defense
        STATE_INFO['IGNORE_P'] = 1 - ((1 - NEW_IGNORE) / (1 - data['IGNORE_P']))

        # 取得原數值
        def getOrigin():
            ORIGIN_ATTRIBUTE = {
                'LEVEL': data['LEVEL'],
                'HP_BASE': (data['LEVEL'] * 90) + 545,
                'HP': data['HP'],
                'STR': data['STR'],
            }
            return ORIGIN_ATTRIBUTE
        
        # 計算等效屬性
        newData = getOrigin()

        print('---------newData---------')
        print(newData)
        print('-------------------------')

        myAttribute = me.calcAttrParam(getOrigin())

        print('---------myAttribute---------')
        print(myAttribute)
        print('-----------------------------')
        
        CLASS_INFO = me.getInfo()
        # --------------------- STR ---------------------
        NEW_AP = myAttribute * IMPROVE_RANGE

        print('---------NEW_AP---------')
        print(NEW_AP)
        print('-----------------------------')

        def getBaseHPByLevel(level):
            return 545 + level * 90
        
        print('---------BaseHP---------')
        print(getBaseHPByLevel(data['LEVEL']))
        print('-----------------------------')
        
        NEW_AP = (NEW_AP - data['STR'] - getBaseHPByLevel(data['LEVEL'])/3.5) * 1.25 * 3.5 + getBaseHPByLevel(data['LEVEL'])
        
        print('---------NEW_AP2---------')
        print(NEW_AP)
        print('-----------------------------')

        # NEW_AP = 新的屬性
        NEW_AP -= data['HP_UNIQUE']
        
        STATE_INFO['HP_CLEAR'] = (NEW_AP / (1 + data['HP_P'])) - data['HP_CLEAR']
        STATE_INFO['HP_P'] = (NEW_AP / data['HP_CLEAR']) - (1 + data['HP_P'])
        STATE_INFO['HP_UNIQUE'] = STATE_INFO['HP_CLEAR'] * (1 + data['HP_P'])
        
        AP_DIFF = myAttribute * (IMPROVE_RANGE - 1)
        NEW_AP = data['STR'] + AP_DIFF
        
        # NEW_AP = 新的屬性
        NEW_AP -= data['STR_UNIQUE']
        STATE_INFO['STR_CLEAR'] = (NEW_AP / (1 + data['STR_P'])) - data['STR_CLEAR']
        STATE_INFO['STR_P'] = (NEW_AP / data['STR_CLEAR']) - (1 + data['STR_P'])
        STATE_INFO['STR_UNIQUE'] = STATE_INFO['STR_CLEAR'] * (1 + data['STR_P'])
        
        # --------------------- 全屬% ---------------------
        # 全屬%
        AP_DIFF = myAttribute * (IMPROVE_RANGE - 1)
        
        # AP差 / (4*淨主屬+副屬)
        STATE_INFO['ALL_P'] = AP_DIFF / data['STR_CLEAR']

        return STATE_INFO
