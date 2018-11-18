#encoding=utf-8
import encrypt_api

from flexx import ui,app,event
class encrypt_decrypt(ui.Widget):
    def init(self):
        with ui.TabLayout():
            self.encrypt = ui.Widget(title='加密')
            with self.encrypt:
                with ui.FormLayout():
                    self.l1 = ui.Label(text='请输入需加密的文本：')
                    self.e1 = ui.LineEdit(title='', text='')
                    self.l2 = ui.Label(text='请输入加密密匙：')
                    self.e2 = ui.LineEdit(title='', text='', password_mode=True)
                    self.l3 = ui.Label(text='请再输入一次加密密匙：')
                    self.e3 = ui.LineEdit(title='', text='', password_mode=True)
                    self.b1 = ui.Button(text='提交')
                    self.l4 = ui.Label(text='')
                    self.l5 = ui.Label(text='')
                    ui.Widget(flex=1)
            self.decrypt = ui.Widget(title='解密')
            with self.decrypt:
                pass
    @event.reaction('b1.pointer_down')
    def calculate_encryp(self, *events):
        if self.e1.text == '' or self.e2.text == '' or self.e3.text == '':
            self.l4.set_text('需加密的文本或密匙不能为空！')
        elif len(self.e1.text) > 10000:
            self.l4.set_text('加密文本字符数应小于10000!')
        elif self.e2.text != self.e3.text:
            self.l4.set_text('两次密码输入不一致！')
        else:
            self.l4.set_text('加密密文为：')
            encrypt_str = encrypt_api.encryption(self.e1.text,self.e2.text)
            self.l5.set_text(encrypt_str)


if __name__ == '__main__':
    ##发布为网页服务时使用
    #app.create_server(host="0.0.0.0",port=12358)
    #app.App(encrypt_decrypt, title='对称加密解密程序').serve()
    #app.start()
    ##桌面程序上面三句话不需要，用下面两句话
    app.App(encrypt_decrypt, title='对称加密解密程序').launch('app', size=(900, 400))
    app.run()