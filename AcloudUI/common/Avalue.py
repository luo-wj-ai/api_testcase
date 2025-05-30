from selenium.webdriver.common.by import By
#登录页面
usename=(By.XPATH,'//input[@placeholder="账号"]')
pw=(By.XPATH,'//input[@placeholder="密码"]')
code=(By.XPATH,'//input[@placeholder="验证码"]')
logins=(By.XPATH,'//span[text()="登 录"]')
'''用户管理'''
#创建用户
usermessage=(By.XPATH,'//span[text()="用户管理"]')
usermessagelist=(By.XPATH,'//span[text()="用户列表"]')
add=(By.XPATH,'//span[text()="新增"]')
usertype=(By.XPATH,'//input[@placeholder="请输入账户类型"]')
phonetype=(By.XPATH,'//span[text()="手机号码"]')
account=(By.XPATH,'//input[@placeholder="请输入用户账号"]')
y=(By.XPATH,'/html/body/div[2]/div/div[3]/div/button[1]')

#查询用户
userselectaccount=(By.XPATH,'//input[@placeholder="请输入账号"]')
userselecta=(By.XPATH,'//span[text()="搜索"]')

#编辑
update=(By.XPATH,'//span[text()="编辑"]')
update2=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div > div:nth-child(2) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input')
choice=(By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[2]')
y2=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')

#重置密码
repassword=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr/td[8]/div/button[2]/span')
newpassword=(By.XPATH,'//input[@placeholder="新密码"]')
newpassword2=(By.XPATH,'//input[@placeholder="请确认密码"]')
y3=(By.CSS_SELECTOR,'body > div:nth-child(9) > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')

#锁定用户
off=(By.XPATH,'//span[text()="锁定"]')
y4=(By.CSS_SELECTOR,'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary')

#解锁用户
on=(By.XPATH,'//span[text()="解锁"]')
y5=(By.CSS_SELECTOR,'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary')

#删除用户
delete=(By.XPATH,'//span[text()="删除"]')
y6=(By.CSS_SELECTOR,'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary')

#查询用户登录日志
logger=(By.XPATH,'//span[text()="用户登录日志"]')
loggeraccount=(By.XPATH,'//input[@placeholder="请输入" and @maxlength="128"]')
loggersele=(By.XPATH,'//span[text()="搜索"]')

#分配云机
cm1=(By.XPATH,'//span[text()="用户云机列表"]')
cm2=(By.XPATH,'//span[text()="新增"]')
cm3=(By.XPATH,'//input[@placeholder="请输入用户账号" and @maxlength="11"]')
cm4=(By.XPATH,'//input[@placeholder="请选择产品"]')
# cm5=(By.XPATH, '//div[@class="el-scrollbar__thumb" and @style="transform: translateY(0%); height: 37.1387%;"]')
cm5=(By.XPATH, '//div[@class="el-scrollbar__thumb" and contains(@style, "transform: translateY(0%); height")]')
# cm6=(By.XPATH,'//span[text()="A2号标准版"]')
cm6=(By.XPATH,'//span[text()="h5570标准版"]')
# cm7=(By.XPATH,'/html/body/div[3]/div/div[2]/form/div[2]/div/div/div[1]/input')
cm7=(By.XPATH,'(//input[@placeholder="请选择"])[3]')
cm8=(By.XPATH,'//div[@class="el-scrollbar__thumb" and contains(@style="transform: translateY(0%); height: 73.0114%;"])')
# cm9=(By.XPATH,'//span[text()="不限时小时卡2"]')
cm9=(By.XPATH,'//span[text()="1块钱"]')
cm10=(By.XPATH,"(//button[contains(@class, 'el-button') and contains(@class, 'el-button--primary') and contains(@class, 'el-button--medium')]/span[text()='确 定'])[9]")
cm11=(By.XPATH,"(//button[contains(@class, 'el-button') and contains(@class, 'el-button--primary') and contains(@class, 'el-button--medium')]/span[text()='确 定'])[4]")

#查询云机列表
cm12=(By.XPATH,'//input[@placeholder="请输入用户账号"]')
cm13=(By.XPATH,'//input[@placeholder="请输入名称"]')
cm14=(By.XPATH,'//span[text()="搜索"]')

#续期云机
cm15=(By.XPATH,'//span[text()="续期"]')
cm16=(By.XPATH,'//input[@placeholder="请选择产品"]')
cm17=(By.XPATH,'//div[@class="el-scrollbar__thumb" and @style="transform: translateY(0%); height: 37.1387%;"]')
cm18=(By.XPATH,'//span[text()="A2号标准版"]')
cm19=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div.el-form-item.is-required.el-form-item--medium > div > div > div > input')
cm20=(By.XPATH,'//div[@class="el-scrollbar__thumb" and @style="transform: translateY(0%); height: 73.0114%;"]')
cm21=(By.XPATH,'//span[text()="不限时小时卡2"]')
cm22=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')
cm23=(By.XPATH,'//*[@id="example"]/div[9]/div/div[3]/span/button[3]')

#变更有效期
cm24=(By.XPATH,'//span[text()="变更有效期"]')
cm25=(By.XPATH,'//input[@placeholder="选择结束时间"]')
cm26=(By.XPATH,'//button[@aria-label="下个月"]')
cm27=(By.XPATH,'//span[text()=20]')
cm28=(By.CSS_SELECTOR,'body > div.el-picker-panel.el-date-picker.el-popper.has-time > div.el-picker-panel__footer > button.el-button.el-picker-panel__link-btn.el-button--default.el-button--mini.is-plain')
cm29=(By.XPATH,'//span[text()="修 改"]')

#查看云机详情
cm30=(By.XPATH,'//span[text()="查看"]')
cm31=(By.CSS_SELECTOR,'#example > div:nth-child(14) > div.el-dialog > div.el-dialog__header > button')

#释放云机
cm32=(By.XPATH,'//span[text()="释放"]')
cm33=(By.CSS_SELECTOR,'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary')


'''订单管理'''
#订单列表查询
ordermessage=(By.XPATH, '//span[text()="订单管理"]')
orderlists=(By.XPATH, '//span[text()="订单列表"]')
orderaccount=(By.XPATH, '//input[@placeholder="请输入账号"]')
ordersele=(By.XPATH, '//span[text()="搜索"]')

'''产品管理'''
#新增产品
product1=(By.XPATH,'//span[text()="产品管理"]')
product2=(By.XPATH,'//span[text()="产品列表"]')
product3=(By.XPATH,'//span[text()="新增"]')
product4=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div:nth-child(1) > div > div > div > input')
product5=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div:nth-child(2) > div > div > div.width-div.el-input.el-input--medium > input')
product6=(By.XPATH,'//input[@placeholder="请输入编码" and @maxlength="20"]')
product7=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(3) > div:nth-child(2) > div > div > div > div > input')
product8=(By.XPATH,'//span[text()="至尊版"]')
product9=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(4) > div:nth-child(1) > div > div > div > div > input')
product10=(By.XPATH,'//span[text()="资源池"]')
product11=(By.XPATH,'//span[text()="合营云-广州4-小盘服务"]')
product12=(By.XPATH,'//input[@max="999999"]')
product13=(By.XPATH,'//input[@placeholder="选择开始时间"]')
product14=(By.XPATH,'//button[@class="el-button el-picker-panel__link-btn el-button--text el-button--mini"]')
product15=(By.XPATH,'//textarea[@placeholder="请输入内容" and @maxlength="255"]')
product16=(By.XPATH,'//span[text()="确 定"]/parent::button[@class="el-button mr20 el-button--primary el-button--medium"]')

#查询产品
product17=(By.XPATH,'//input[@placeholder="请输入名称" and @maxlength="32"]')
product18=(By.XPATH,'//input[@placeholder="全部"]')
product19=(By.XPATH,'//span[text()="草稿"]')
product20=(By.XPATH,'//span[text()="搜索"]')

#编辑产品
product21=(By.XPATH,'//span[text()="编辑"]')
product22=product4
product23=product5
product24=(By.XPATH,'//button[@class="el-button mr20 el-button--primary el-button--medium"]')

#删除产品
product25=(By.XPATH,'//span[text()="返回"]')
product26=(By.XPATH,'//span[text()="删除"]/parent::button[@class="el-button el-button--text el-button--mini"]')
product27=(By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')

#新增单品
productitem1=(By.XPATH,'//span[text()="产品详情"]')
productitem2=(By.XPATH,'//button[@class="el-button el-button--primary el-button--mini is-plain"]')
productitem3=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div:nth-child(1) > div > div > div.el-input.el-input--medium > input')
productitem4=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div:nth-child(2) > div > div > div > input')
productitem5=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div:nth-child(3) > div > div > div > input')
productitem6=(By.XPATH,'//input[@placeholder="选择开始时间"]')
productitem7=(By.XPATH,'//button[@class="el-button el-picker-panel__link-btn el-button--text el-button--mini"]')
productitem8=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(4) > div > div > div > div.el-textarea.el-input--medium > textarea')
productitem9=(By.XPATH,'//input[@maxlength="8"]')
productitem10=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(7) > div.el-col.el-col-12 > div > div > div > div.el-input.el-input--medium.el-input--suffix > input')
productitem11=(By.XPATH,'//span[text()="天"]')
productitem12=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(8) > div:nth-child(1) > div > div > div.el-input.el-input--medium > input')
productitem13=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(10) > div > div > div > div.el-textarea.el-input--medium > textarea')
productitem14=(By.XPATH,'//span[text()="保存"]')

#编辑单品
productitem15=(By.XPATH,'//span[text()="编辑"]')
productitem16=productitem3
productitem17=productitem4
productitem18=(By.XPATH,'//span[text()="保存"]')

#删除单品
productitem19=(By.XPATH,'//span[text()="删除"]/parent::button[@class="el-button el-button--text el-button--mini"]')
productitem20=(By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')


#新增兑换码批次
redeemcode1=(By.XPATH,'//span[text()="兑换码批次"]')
redeemcode2=(By.XPATH,'//span[text()="新增"]')
redeemcode3=(By.XPATH,'//div[@style="width: 220px;"]/child::input[@maxlength="32"]')
redeemcode4=(By.XPATH,'//input[@placeholder="请选择产品"]')
redeemcode5=(By.XPATH,'//div[@class="el-scrollbar__thumb" and @style="transform: translateY(0%); height: 73.0114%;"]')
redeemcode6=(By.XPATH,'//span[text()="A2号标准版"]')
redeemcode7=(By.CSS_SELECTOR,'#dialog > div > div.el-dialog__body > form > div:nth-child(3) > div > div > div > input')
redeemcode8=(By.XPATH,'//div[@class="el-scrollbar__thumb" and @style="transform: translateY(0%); height: 49.2337%;"]')
redeemcode9=(By.XPATH,'//span[text()="不限时小时卡"]')
redeemcode10=(By.CSS_SELECTOR,'#dialog > div > div.el-dialog__body > form > div:nth-child(4) > div > div > div > input')
redeemcode11=(By.XPATH,'//span[text()="预生成"]')
redeemcode12=(By.XPATH,'//input[@maxlength="6"]')
redeemcode13=(By.XPATH,'//input[@placeholder="选择开始时间"]')
redeemcode14=(By.XPATH,'//button[@class="el-button el-picker-panel__link-btn el-button--text el-button--mini"]')
redeemcode15=(By.XPATH,'//input[@placeholder="选择结束时间"]')
redeemcode16=(By.XPATH,'//div[contains(@style,"position: fixed;")]//div[@class="el-picker-panel__body-wrapper"]//div[@class="el-date-picker__header"]//button[@aria-label="下个月"]')
redeemcode17=(By.XPATH,'//div[contains(@style,"position: fixed;")]//div[@class="el-picker-panel__body-wrapper"]//table[@class="el-date-table"]//span[text()=20]')
redeemcode18=(By.XPATH,'//div[contains(@style,"position: fixed;")]//div[@class="el-picker-panel__footer"]//button[@class="el-button el-picker-panel__link-btn el-button--default el-button--mini is-plain"]')
redeemcode19=(By.XPATH,'//input[@maxlength="5"]')
redeemcode20=(By.XPATH,'//button[@class="el-button el-button--primary el-button--medium"]')

#生成兑换码批次
redeemcode21=(By.XPATH,'//div[@style="width: 240px;"]/child::input[@placeholder="请输入名称"]')
redeemcode22=(By.XPATH,'//span[text()="搜索"]')
redeemcode23=(By.XPATH,'//span[text()="生成"]')
redeemcode24=(By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')

#新增特权
privilege1=(By.XPATH,'//span[text()="会员中心"]')
privilege2=(By.XPATH,'//span[text()="特权管理"]')
privilege3=(By.XPATH,'//span[text()="新增"]')
privilege4=(By.XPATH,'//input[@placeholder="请输入特权名" and @maxlength="20"]')
privilege5=(By.XPATH,'//input[@placeholder="请输入特权说明" and @maxlength="20"]')
privilege6=(By.CSS_SELECTOR,'#dialog > div > div.el-dialog__body > form > div:nth-child(3) > div > div > div:nth-child(1) > div > button')
privilege7=(By.XPATH,'//button[@class="el-button el-button--primary el-button--medium"]')


#查询特权
privilege8=(By.XPATH,'//input[@placeholder="请输入特权名" and @maxlength="32"]')
privilege9=(By.XPATH,'//span[text()="搜索"]')

#编辑特权
privilege10=(By.XPATH,'//span[text()="编辑"]')
privilege11=privilege4
privilege12=privilege7

#删除特权
privilege13=(By.XPATH,'//span[text()="删除"]/parent::button[@class="el-button el-button--text el-button--mini"]')
privilege14=(By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')

#新增会员套餐管理
membermenu1=(By.XPATH,'//span[text()="会员套餐管理"]')
membermenu2=(By.XPATH,'//span[text()="新增"]')
membermenu3=(By.XPATH,'//input[@placeholder="请输入标题"]')
membermenu4=(By.CSS_SELECTOR,'#dialog > div > div.el-dialog__body > form > div:nth-child(2) > div:nth-child(1) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input')
membermenu5=(By.XPATH,'//div[@style="transform: translateY(0%); height: 37.1387%;"]')
membermenu6=(By.XPATH,'//li[text()=" A2号标准版(100025622) "]')
membermenu7=(By.CSS_SELECTOR,'#dialog > div > div.el-dialog__body > form > div:nth-child(2) > div:nth-child(2) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input')
membermenu8=(By.XPATH,'//div[@style="transform: translateY(0%); height: 73.0114%;"]')
membermenu9=(By.XPATH,'//li[text()="不限时小时卡2(100066998672)"]')
membermenu10=(By.XPATH,'//input[@placeholder="开始时间"]')
membermenu11=(By.XPATH,'//button[@class="el-button el-picker-panel__link-btn el-button--text el-button--mini"]')
membermenu12=(By.XPATH,'//input[@placeholder="结束时间"]')
membermenu13=(By.XPATH,'//div[contains(@style,"position: fixed;")]//div[@class="el-picker-panel__body-wrapper"]//div[@class="el-date-picker__header"]//button[@aria-label="下个月"]')
membermenu14=(By.XPATH,'//div[contains(@style,"position: fixed;")]//div[@class="el-picker-panel__body-wrapper"]//table[@class="el-date-table"]//span[text()=20]')
membermenu15=(By.XPATH,'//div[contains(@style,"position: fixed;")]//div[@class="el-picker-panel__footer"]//button[@class="el-button el-picker-panel__link-btn el-button--default el-button--mini is-plain"]')
membermenu16=(By.CSS_SELECTOR,'#dialog > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')

#查询会员套餐管理
membermenu17=(By.XPATH,'//input[@placeholder="请输入"]')
membermenu18=(By.XPATH,'//span[text()="搜索"]')

#编辑会员套餐管理
membermenu19=(By.XPATH,'//span[text()="编辑"]')
membermenu20=membermenu3
membermenu21=(By.CSS_SELECTOR,'#dialog > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')

#删除会员套餐管理
membermenu22=(By.XPATH,'//button[@class="el-button el-button--text el-button--mini"]/child::span[text()="删除"]')
membermenu23=(By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')


'''运营管理'''
#广告管理-新增广告
adverse1=(By.XPATH,'//span[text()="运营管理"]')
adverse2=(By.XPATH,'//span[text()="广告管理"]')
adverse3=(By.XPATH,'//*[@id="advertise"]/ul/li[5]')
adverse4=(By.XPATH,'//span[text()="新增"]')
adverse5=(By.XPATH,'//input[@placeholder="请输入标题名称"]')
adverse6=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div.el-input.el-input--medium.el-input--suffix > input')
adverse7=(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper.is-multiple > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)')
adverse8=(By.XPATH,'//textarea[@placeholder="请输入内容"]')
adverse9=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(4) > div > div:nth-child(1) > div > button')
adverse10=(By.XPATH,'//*[@id="unchange"]/div/div/div[1]/input')
adverse11=(By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[1]')
adverse12=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')
#搜索广告
adverse101=(By.XPATH,'//input[@placeholder="请输入标题"]')
adverse102=(By.XPATH,'//span[text()="搜索"]')
#编辑广告
adverse13=(By.XPATH,'//*[@id="advertise"]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[11]/div/button[1]')
adverse14=(By.XPATH,'//input[@placeholder="请输入标题名称"]')
adverse15=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')
#删除广告
adverse16=(By.XPATH,'//*[@id="advertise"]/div[3]/div[1]/div[3]/table/tbody/tr/td[11]/div/button[4]')
adverse17=(By.CSS_SELECTOR,'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary')

#新增配置
config1=(By.XPATH,'//span[text()="配置管理"]')
config2=(By.XPATH,'//li[text()="版本配置"]')
config3=(By.XPATH,'//button[@class="el-button el-button--primary el-button--mini is-plain"]')
config4=(By.XPATH,'//input[@placeholder="请输入安装包名称"]')
config5=(By.XPATH,'//input[@placeholder="格式为x.x.x.x"]')
config6=(By.XPATH,'//input[@placeholder="版本号为数字类型"]')
config7=(By.XPATH,'//input[@placeholder="请输入下载地址"]')
config8=(By.XPATH,'//input[@placeholder="请输入安装包大小"]')
config9=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div:nth-child(1) > div > div > div > div.el-input.el-input--medium.el-input--suffix > input')
config10=(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)')
config11=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div:nth-child(2) > div > div > div > div > input')
config12=(By.XPATH,'//span[text()="否"]')
config13=(By.XPATH,'//textarea[@placeholder="请输入版本描述内容"]')
config14=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')

#查询配置
config15=(By.CSS_SELECTOR,'#advertise > div:nth-child(3) > form > div:nth-child(1) > div > div > input')
config16=(By.CSS_SELECTOR,'#advertise > div:nth-child(3) > form > div:nth-child(6) > div > button.el-button.el-button--primary.el-button--mini')

#编辑配置
config17=(By.XPATH,'//*[@id="advertise"]/div[2]/div[3]/div[3]/table/tbody/tr/td[13]/div/button[2]/span')
config18=config4
config19=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')

#删除配置
config20=(By.XPATH,'//*[@id="advertise"]/div[2]/div[3]/div[3]/table/tbody/tr/td[13]/div/button[3]/span')
config21=(By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary " ]')

#功能引导管理-新增功能引导
guide1=(By.XPATH,'//span[text()="功能引导管理"]')
guide2=(By.XPATH,'//span[text()="新增"]')
guide3=(By.XPATH,'//input[@class="el-input__inner" and @minlength="4"]')
guide4=(By.XPATH,'//div[@class="el-upload el-upload--picture-card"]')
guide5=(By.CSS_SELECTOR,'#app > div > div.main-container > section > div > div:nth-child(5) > div > div.el-dialog__body > form > div:nth-child(3) > div > div > div.el-col.el-col-10 > div > input')
guide6=(By.XPATH,'//span[text()="搜索产品"]')
guide7=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[4]/div/div/div[1]/div[1]/div[1]/label/span/span')

guide8=(By.XPATH,'//span[text()="确定"]')

#功能引导管理-搜索功能引导
guide9=(By.XPATH,'//input[@placeholder="请输入功能引导名称 "]')
guide10=(By.XPATH,'//span[text()="搜索"]')

#功能引导管理-编辑功能引导
guide11=(By.XPATH,'//span[text()="编辑"]')
guide12=(By.XPATH,'//input[@class="el-input__inner" and @minlength="4"]')
guide13=(By.XPATH,'//span[text()="确定"]')
#功能引导管理-删除功能引导
guide14=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[1]/div/label/span/span')
guide15=(By.XPATH,'//span[text()="批量删除"]')
guide16=(By.CSS_SELECTOR,'#app > div > div.main-container > section > div > div:nth-child(6) > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')

#开屏动画管理-新增开屏动画
screen1=(By.XPATH,'//span[text()="开屏动画管理"]')
screen2=guide2
screen3=guide3
screen4=guide4
screen5=(By.CSS_SELECTOR,'#app > div > div.main-container > section > div > div:nth-child(5) > div > div.el-dialog__body > form > div:nth-child(4) > div > div > div.el-col.el-col-10 > div > input')
screen6=guide6
screen7=(By.CSS_SELECTOR,'#app > div > div.main-container > section > div > div:nth-child(5) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div.el-tree > div.el-tree-node.is-expanded.is-focusable > div.el-tree-node__content > label > span > span')
screen8=guide8
#开屏动画管理-搜索开屏动画
screen9=(By.XPATH,'//input[@placeholder="请输入开屏动画名称 "]')
screen10=guide10
#开屏动画管理-编辑开屏动画
screen11=guide11
screen12=guide12
screen13=guide13
#开屏动画管理-删除开屏动画
screen14=guide14
screen15=guide15
screen16=guide16

#灵犀助手管理-新增灵犀助手
lingxi1=(By.XPATH,'//span[text()="灵犀助手管理"]')
lingxi2=guide2
lingxi3=(By.XPATH,'//input[@placeholder="请输入配置名称" and @minlength="4"]')
lingxi4=(By.CSS_SELECTOR,'#app > div > div.main-container > section > div > div:nth-child(5) > div > div.el-dialog__body > form > div:nth-child(2) > form > div:nth-child(1) > label > span.el-checkbox__input > span')
lingxi5=(By.CSS_SELECTOR,'#app > div > div.main-container > section > div > div:nth-child(5) > div > div.el-dialog__body > form > div:nth-child(2) > form > div.el-form-item.upload-img.el-form-item--mini > div > ul > li > div > div')
lingxi6=(By.CSS_SELECTOR,'#app > div > div.main-container > section > div > div:nth-child(5) > div > div.el-dialog__body > form > div:nth-child(2) > form > div:nth-child(3) > div > div > input')
lingxi7=(By.CSS_SELECTOR,'#app > div > div.main-container > section > div > div:nth-child(5) > div > div.el-dialog__body > form > div:nth-child(4) > div > div > div.el-col.el-col-10 > div > input')
lingxi8=guide6
lingxi9=(By.CSS_SELECTOR,'#app > div > div.main-container > section > div > div:nth-child(5) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div.el-tree > div.el-tree-node.is-expanded.is-focusable > div.el-tree-node__content > label > span > span')
lingxi10=guide8

#灵犀助手管理-搜索灵犀助手
lingxi11=(By.XPATH,'//input[@placeholder="请输入名称 "]')
lingxi12=guide10

#灵犀助手管理-编辑灵犀助手
lingxi13=guide11
lingxi14=(By.XPATH,'//input[@placeholder="请输入配置名称"]')
lingxi15=guide13

#灵犀助手管理-删除灵犀助手
lingxi16=guide14
lingxi17=guide15
lingxi18=guide16

'''OS运营管理'''
#新增OS广告
OSadverse1=(By.XPATH,'//span[text()="OS运营管理"]')
OSadverse2=(By.XPATH,'//span[text()="广告管理"]/parent::div[@class="el-submenu__title"]')
OSadverse3=(By.XPATH,'//span[text()="广告配置"]')
OSadverse4=(By.XPATH,'//button[@class="el-button el-button--primary el-button--mini is-plain"]')
OSadverse5=(By.XPATH,'//input[@placeholder="请选择广告位"]/parent::div[@class="el-input el-input--medium el-input--suffix"]')
OSadverse6=(By.XPATH,'//span[@class="banner-span2 banner-spanName" and text()="自动化测试"]')
OSadverse7=(By.XPATH,'//div[@class="el-input el-input--medium el-input--suffix"]/input[@placeholder="请选择广告类型"]')
OSadverse8=(By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[6]')
OSadverse9=(By.XPATH,'//input[@placeholder="请输入广告标题"]')
OSadverse10=(By.XPATH,'//span[@class="el-radio__inner"]/parent::span[@class="el-radio__input"]')
OSadverse11=(By.XPATH,'//input[@placeholder="请输入跳转链接"]')
OSadverse12=(By.XPATH,'//span[text()="下一步"]')
OSadverse13=(By.XPATH,'//span[text()="确 定"]/parent::button[@class="el-button mr20 el-button--primary el-button--medium"]')

#查询OS广告
OSadverse14=(By.XPATH,'//input[@placeholder="请选择广告位"]/parent::div[@class="el-input el-input--small el-input--suffix"]')
OSadverse15=(By.XPATH,'//span[text()="自动化测试" and @class="banner-css"]')
OSadverse16=(By.XPATH,'//span[text()="搜索"]')

#编辑OS广告
OSadverse17=(By.XPATH,'//span[text()="编辑"]')
OSadverse18=OSadverse9
OSadverse19=OSadverse12
OSadverse20=OSadverse13
#删除OS广告
OSadverse21=(By.XPATH,'//span[text()="删除"]/parent::button[@class="el-button el-button--text el-button--mini"]')
OSadverse22=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper.post-diaolog > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium')

#新增主题
theme1=(By.XPATH,'//span[text()="主题管理"]')
theme2=(By.XPATH,'//span[text()="新增"]')
theme3=(By.XPATH,'//input[@maxlength="20"]')
theme4=(By.XPATH,'//div[@class="el-upload el-upload--picture-card"]')
theme5=(By.XPATH,'//button[@class="el-button el-button--default el-button--small"]')
theme6=OSadverse12
theme7=OSadverse13

#查询主题
theme8=(By.XPATH,'//input[@placeholder="请输入"]')
theme9=OSadverse16

#编辑主题
theme10=(By.XPATH,'//span[text()="编辑"]')
theme11=theme3
theme12=theme6
theme13=theme7

#删除主题
theme14=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/table/thead/tr/th[1]/div/label/span/span')
theme15=(By.XPATH,'//span[text()="删除"]')
theme16=(By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')

#新增壁纸
wallpaper1=(By.XPATH,'//span[text()="壁纸管理"]')
wallpaper2=(By.XPATH,'//span[text()="新增"]')
wallpaper3=(By.XPATH,'//div[@class="el-input el-input--medium"]/child::input[@maxlength="20" and @placeholder="请输入"]')
wallpaper4=(By.XPATH,'//div[@class="el-upload el-upload--picture-card"]')
wallpaper5=OSadverse12
wallpaper6=OSadverse13

#查询壁纸
wallpaper7=(By.XPATH,'//div[@class="el-input el-input--small el-input--suffix"]/child::input[@maxlength="128"]')
wallpaper8=OSadverse16
#编辑壁纸
wallpaper9=(By.XPATH,'//span[text()="编辑"]')
wallpaper10=(By.XPATH,'//input[@maxlength="20"]')
wallpaper11=OSadverse12
wallpaper12=OSadverse13
#删除壁纸
wallpaper13=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/table/thead/tr/th[1]/div/label/span/span')
wallpaper14=(By.XPATH,'//span[text()="删除"]')
wallpaper15=(By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')

#新增小组件
widget1=(By.XPATH,'//span[text()="小组件管理"]')
widget2=(By.XPATH,'//span[text()="新增"]')
widget3=(By.XPATH,'//div[@class="el-input el-input--medium"]/child::input[@maxlength="20" and @placeholder="请输入"]')
widget4=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div.el-input.el-input--medium.el-input--suffix > input')
widget5=(By.XPATH,'//span[text()="2*2"]')
widget6=(By.XPATH,'//div[@class="el-upload el-upload--picture-card"]')
widget7=OSadverse12
widget8=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.mr20.el-button--primary.el-button--medium')

#查询小组件
widget9=(By.XPATH,'//div[@class="el-input el-input--small el-input--suffix"]/child::input[@maxlength="128"]')
widget10=OSadverse16
#编辑小组件
widget11=(By.XPATH,'//span[text()="编辑"]')
widget12=widget3
widget13=OSadverse12
widget14=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.mr20.el-button--primary.el-button--medium')

#删除小组件
widget15=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/table/thead/tr/th[1]/div/label/span/span')
widget16=(By.XPATH,'//span[text()="删除"]')
widget17=(By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')


#新增应用
application1=(By.XPATH,'//span[text()="应用管理"]')
application2=(By.XPATH,'//span[text()="上传应用 "]')
application3=(By.XPATH,'//button[@class="el-button el-button--primary el-button--medium"]')
application4=(By.XPATH,'//input[@placeholder="请输入应用名称"]')
application5=(By.XPATH,'//div[@class="el-upload el-upload--picture-card"]')
application6=(By.XPATH,'//span[text()="确 定"]')

#查询应用
application7=(By.XPATH,'//input[@placeholder="请输入"]')
application8=(By.XPATH,'//span[text()="搜索"]')

#删除应用
application9=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/table/thead/tr/th[1]/div/label/span/span')
application10=(By.XPATH,'//span[text()="删除应用"]')
application11=(By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')


#新增消息
message1=(By.XPATH,'//span[text()="消息管理"]')
message2=(By.XPATH,'//span[text()="消息列表"]')
message3=(By.XPATH,'//span[text()="新增"]')
message4=(By.XPATH,'//input[@placeholder="请输入消息标题"]')
message5=(By.XPATH,'//textarea[@maxlength="255"]')
message6=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(5) > div > div > div > input')
message7=(By.XPATH,'//span[text()="部分用户"]')
message8=(By.XPATH,'//span[text()="添加"]')
message9=(By.XPATH,'//input[@placeholder="请输入账号"]')
message10=(By.XPATH,'//span[text()=" 搜索 "]')
message11=(By.XPATH,'//span[@class="el-checkbox__inner"]')
message12=(By.XPATH,'//div[@aria-label="用户列表"]//div[@class="el-dialog__footer"]//button[@class="el-button el-button--primary el-button--medium"]')
message13=(By.XPATH,'//div[@aria-label="新增消息"]//div[@class="el-dialog__footer"]//button[@class="el-button el-button--primary el-button--medium"]')