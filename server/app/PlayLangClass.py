import subprocess
from subprocess import PIPE,TimeoutExpired
import asyncio

import docker

class PlayLangClass:

    def __init__(self, code, input, lang):
        self.code = code
        self.input = input
        self.lang = lang
        self.dir_name = './run-scripts/'

    def main(self):
        if not self.code or not self.lang:
            return {'out': "",'err': ""}
        loop = asyncio.new_event_loop()
        loop.create_task(self.write_code(self.code,self.lang,self.input))
        result = loop.run_until_complete(self.run_code(self.lang))
        return result

    async def write_code(self, code,lang,input):
        langFile = self.select_lang(lang)
        ## コードをファイルに書き込む
        text_file = open(self.dir_name + "main." + langFile, "wt")
        text_file.write(code)
        ## inputを与える
        text_file = open(self.dir_name + "input.txt", "wt")
        text_file.write(input)
    
    async def run_code(self, lang):
        try:
            client = docker.from_env()
            result = client.containers.get(f"playground-{lang}").exec_run(cmd=["sh", f"{lang}.sh"])
            out = ""
            err = ""
            if result.exit_code == 0:
                out = result.output.decode('utf-8')
            else:
                err = result.output.decode('utf-8') # エラーメッセージ
        except TimeoutExpired as e:
            print(f"ERROR : {e}")
            err = "ERROR : " + str(e) + "\nMessage : 100秒以内で実行できるコードにしてください。"
            out = ""
        return {'out': out,'err': err}

    def select_lang(self, lang):
        langFile = ""
        if lang == 'perl':
            langFile = "pl"
        elif lang == 'go':
            langFile = "go"
        elif lang == 'kotlin':
            langFile = "kt"
        elif lang == 'julia':
            langFile = "jl"
        elif lang == "rust":
            langFile = "rs"
        elif lang == "python":
            langFile = "py"
        elif lang == "swift":
            langFile = "swift"
        return langFile
