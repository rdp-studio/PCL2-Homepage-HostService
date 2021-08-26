# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,jsonify,redirect,Blueprint,abort
from pathlib import Path
import random

app = Flask(__name__)

print("\033[45mPCL2-Homepage-HostService\033[0m" + "  " + "\033[46mPowerd By RDPStudio\033[0m")
print("\n")
#print("\033[46m" + "" + "\033[0m")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/write', methods=['POST'])
def write():
    t = request.form['type']
    if t == "create":
        d = random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"]) + random.choice(["你好","世界","地球","宇宙","太阳系","你","我","他","这","上","下","左","右"])
        try:
            n1 = request.form['name']
            c1 = request.form['code']
            my_file = Path("./storage/" + n1 + ".txt")
            if my_file.is_file():
                return "名称已被使用，请更换。"
            with open('./storage/' + n1 + '.txt', 'w', encoding="utf-8") as f:
                f.write(c1)
            with open('./storage/' + n1 + '.k.txt', 'w', encoding="utf-8") as f:
                f.write(d)
            return "主页创建成功！你的订阅地址（因为服务器也跑着frp所以就暂用这个域名了）：http://frp.rdpstudio.top:233/sub?s=" + str(n1) + " 这是修改密钥：" + str(d) + " 请妥善保管。"
        except:
            return "出现问题。请联系邮箱admin@rdpstudio.top紧急修复！"
    elif t == "edit":
        try:
            n1 = request.form['name']
            c1 = request.form['code']
            k1 = request.form['key']
            with open('./storage/' + n1 + '.k.txt', encoding="utf-8") as f:
                k2 = f.read()
            if not k1 == k2:
                return "你！没有权限！"
            with open('./storage/' + n1 + '.txt', 'w', encoding="utf-8") as f:
                f.write(c1)
            return "主页修改成功！你的订阅地址（因为服务器也跑着frp所以就暂用这个域名了）：http://frp.rdpstudio.top:233/sub?s=" + str(n1)
        except:
            return "出现问题（大概是你填错名称了吧。。。）。如果不是，请联系邮箱admin@rdpstudio.top紧急修复！"

@app.route('/sub')
def sub():
    try:
        with open('./storage/' + request.args.get('s') + '.txt', encoding="utf-8") as f:
            sub = f.read()
    except:
        abort(500)
    sub = sub + "\n" + '''<Grid Margin="0,0,0,15">
		<Grid.ColumnDefinitions>
			<ColumnDefinition Width="1*"></ColumnDefinition>
			<ColumnDefinition Width="100"></ColumnDefinition>
			<ColumnDefinition Width="1*"></ColumnDefinition>
		</Grid.ColumnDefinitions>
		<Line X1="0" X2="100" Stroke="{DynamicResource ColorBrush5}" StrokeThickness="1.5" HorizontalAlignment="Center" Stretch="Fill" Grid.Column="0" />
		<TextBlock Text="免 费 PCL2 主 页 托 管" HorizontalAlignment="Center" FontSize="14" Foreground="{DynamicResource ColorBrush5}" Grid.Column="1" VerticalAlignment="Center" />
		<Line X1="0" X2="100" Stroke="{DynamicResource ColorBrush5}" StrokeThickness="1.5" HorizontalAlignment="Center" Stretch="Fill" Grid.Column="2" />
	</Grid>
<StackPanel Margin="0,10,0,20" HorizontalAlignment="Center" Orientation="Horizontal">
	<local:MyButton Width="300" Height="35" Padding="13,0,13,0" Text="免费托管我的主页！" Margin="0,0,10,0" EventType="打开网页" EventData="http://frp.rdpstudio.top:233" ToolTip="点击免费托管你的主页" />
	<local:MyButton Width="200" Height="35" Padding="13,0,13,0" Text="刷新主页" EventType="刷新主页" Margin="0,0,10,0" ToolTip="点击刷新" />
	<local:MyButton Width="200" Height="35" Padding="13,0,13,0" Text="托管服务反馈" EventType="打开网页" EventData="https://github.com/rdp-studio/PCL2-Homepage-HostService/issues/new" ToolTip="点击前往 Github 提交反馈" />
</StackPanel>
<Border Background="#CCFFFFFF" Height="140" Margin="-25,30,-25,-10" BorderThickness="0,2,0,0" BorderBrush="#AAAAAAAA">
	<StackPanel Margin="40,15,0,10">
		<TextBlock Text="由 免费PCL2主页托管 提供托管支持" FontSize="16" Margin="0,5,5,5" />
		<TextBlock Text="托管服务By：RDPStudio" />

		<StackPanel Orientation="Horizontal" Margin="0,2,0,0">
			<TextBlock Text="托管服务Github:  " />
			<local:MyTextButton Text="https://github.com/rdp-studio/PCL2-Homepage-HostService" EventType="打开网页" EventData="https://github.com/rdp-studio/PCL2-Homepage-HostService" ToolTip="点击打开Github" />
		</StackPanel>

		<StackPanel Margin="0,10,0,0" Orientation="Horizontal">
			<TextBlock Text="无特殊声明本主页采用 " />
			<local:MyTextButton Text="CC BY-NC-SA 3.0" EventType="打开网页" EventData="https://creativecommons.org/licenses/by-nc-sa/3.0/ " />
			<TextBlock Text=" 授权。(PCL2主页免费托管服务不为此主页担保,若有任何违规信息请点击上方反馈按钮举报)" />
		</StackPanel>
	</StackPanel>
</Border>
'''
    return sub

if (__name__ == "__main__"):
    app.run(host = '0.0.0.0', port = 233, debug=False)
