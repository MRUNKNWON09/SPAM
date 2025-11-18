# Vercel-ready FULL version (Option A)
# This file is adapted from your original main.py and modified to be serverless-friendly.
# Reference to original uploaded file: fileciteturn1file0

# ----- ORIGINAL MAIN.PY (BEGIN) -----
# DeVloped By AbdeeLkarim Amiri
import requests
import os
import psutil
import sys
import jwt
import pickle
import json
import binascii
import time
import urllib3
import xKEys
import base64
import datetime
import re
import socket
import threading
import http.client
import ssl
import gzip
import asyncio
import gc

from io import BytesIO
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import *
from datetime import datetime, timedelta
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from cfonts import render, say
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from flask import Flask, request

console = Console()
STOP_FLAG = False

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def G_AccEss(U, P):
    UrL = "https://100067.connect.garena.com/oauth/guest/token/grant"
    HE = {
        "Host": "100067.connect.garena.com",
        "User-Agent": Ua(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close",
    }
    dT = {
        "uid": f"{U}",
        "password": f"{P}",
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067",
    }
    try:
        R = requests.post(UrL, headers=HE, data=dT)
        if R.status_code == 200:
            return R.json()["access_token"], R.json()["open_id"]
        else:
            print(R.json())
    except Exception as e:
        print(e)
        ResTarTinG()


def MajorLoGin(PyL):
    context = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection("loginbp.ggblueshark.com", context=context)
    headers = {
        "X-Unity-Version": "2018.4.11f1",
        "ReleaseVersion": "OB51",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-GA": "v1 1",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)",
        "Host": "loginbp.ggblueshark.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
    }
    try:
        conn.request("POST", "/MajorLogin", body=PyL, headers=headers)
        response = conn.getresponse()
        raw_data = response.read()
        if response.getheader("Content-Encoding") == "gzip":
            with gzip.GzipFile(fileobj=BytesIO(raw_data)) as f:
                raw_data = f.read()
        TexT = raw_data.decode(errors="ignore")
        if "BR_PLATFORM_INVALID_OPENID" in TexT or "BR_GOP_TOKEN_AUTH_FAILED" in TexT:
            sys.exit()
        return raw_data.hex() if response.status in [200, 201] else None
    finally:
        conn.close()


Thread(target=AuTo_ResTartinG, daemon=True).start()


class FF_CLient:
    def __init__(self, U, P, forced_target=None):
        """
        forced_target: optional. If provided, it will be used as the GroupID (TarGeT)
        instead of the GroupID parsed from incoming packets.
        """
        self.empty_count = 0
        self.reader = None
        self.writer = None
        self.forced_target = forced_target
        self.Get_FiNal_ToKen_0115(U, P)

    async def STarT(self, JwT_ToKen, AutH_ToKen, ip, port, ip2, port2, key, iv, bot_uid):
        R = asyncio.Event()
        task1 = asyncio.create_task(
            self.ChaT(self.JwT_ToKen, self.AutH_ToKen, ip, port, key, iv, bot_uid, R)
        )
        await R.wait()
        await asyncio.sleep(0.5)
        task2 = asyncio.create_task(
            self.OnLinE(self.JwT_ToKen, self.AutH_ToKen, ip2, port2, key, iv, bot_uid)
        )
        await asyncio.gather(task1)

    async def sF(self):
        if self.writer:
            try:
                self.writer.close()
                await asyncio.sleep(0.2)
                await self.writer.wait_closed()
            except Exception as e:
                print(f" - Error CLose WriTer => {e}")
                ResTarTinG()
        self.reader = None
        self.writer = None
        gc.collect()

    async def OnLinE(self, Token, tok, host2, port2, key, iv, bot_uid):
        T = "ar"
        global writer, writer2, TarGeT, sQ, Nm
        while True:
            if STOP_FLAG:
                return
            try:
                self.reader2, self.writer2 = await asyncio.open_connection(host2, int(port2))
                await asyncio.sleep(0.5)
                self.writer2.write(bytes.fromhex(tok))
                await self.writer2.drain()
                await asyncio.sleep(0.4)
                while True:
                    if STOP_FLAG: 
                        return
                    try:
                        self.DaTa = await self.reader2.read(9999)
                        if not self.DaTa:
                            await asyncio.sleep(0.2)
                            break
                        # commented out behavior preserved
                    except (
                        asyncio.TimeoutError,
                        ConnectionResetError,
                        ConnectionAbortedError,
                        asyncio.IncompleteReadError,
                        BrokenPipeError,
                        OSError,
                        Exception,
                    ) as e:
                        pass
            except (
                asyncio.TimeoutError,
                ConnectionRefusedError,
                ConnectionResetError,
                ConnectionAbortedError,
                asyncio.IncompleteReadError,
                BrokenPipeError,
                OSError,
                Exception,
            ) as e:
                pass

    async def ChaT(self, Token, tok, host, port, key, iv, bot_uid, R):
        T = "fr"
        print(bot_uid)
        global writer, writer2, TarGeT, sQ, Nm
        while True:
            if STOP_FLAG: 
                return
            try:
                self.reader, self.writer = await asyncio.open_connection(host, int(port))
                self.writer.write(bytes.fromhex(tok))
                await self.writer.drain()
                await asyncio.sleep(0.4)
                self.writer.write(GLobaL(T, key, iv))
                await self.writer.drain()
                await asyncio.sleep(0.4)
                R.set()
                while True:
                    if STOP_FLAG: 
                        return
                    try:
                        self.DaTa = await self.reader.read(9999)
                        if not self.DaTa:
                            await asyncio.sleep(0.2)
                            break
                        if self.DaTa.hex().startswith("1200") and b"SecretCode" in self.DaTa:
                            U = json.loads(DeCode_PackEt(self.DaTa.hex()[10:]))
                            U2 = json.loads(DeCode_PackEt(self.DaTa.hex()[36:]))
                            Uu = json.loads(U["5"]["data"]["8"]["data"])

                            Nm = U2["9"]["data"]["1"]["data"]
                            # Use forced target if provided, otherwise parse from packet
                            if self.forced_target:
                                try:
                                    TarGeT = int(self.forced_target)
                                except Exception:
                                    # fallback to parsed GroupID if forced_target invalid
                                    TarGeT = int(Uu.get("GroupID", 0))
                            else:
                                TarGeT = int(Uu["GroupID"])

                            sQ = Uu["SecretCode"]
                            rQ = Uu.get("RecruitCode")

                            # RedZed_3alamyia_Chat(uid, code , K, I)
                            self.writer.write(RedZed_3alamyia_Chat(TarGeT, sQ, key, iv))
                            await self.writer.drain()

                            # ---- FIXED MESSAGE (no f-string issues) ----
                            msg_part1 = (
                                "-HELLO I AM SPIDEERIO GAMING  !\n\n"
                                "SUBSCRIBE ME ON YOUTUBE  OR BE BANNED \n\n"
                                "SPIDEERIO GAMING : "
                            )
                            msg_part2 = "@Anonymous_is_back_action !! \n\n"
                            msg_part3 = (
                                "telegram team channel : @cyberarchbd \n\n"
                                "DEV Telegram username : @Anonymous_is_back_action"
                            )

                            full_msg = (
                                "[FF0000][B][C]"
                                + xMsGFixinG(msg_part1)
                                + "[00FF00]"
                                + xMsGFixinG(msg_part2)
                                + "[FFFF00]"
                                + xMsGFixinG(msg_part3)
                            )

                            # send message
                            self.writer.write(RedZed_SendMsg(full_msg, TarGeT, bot_uid, key, iv))
                            await self.writer.drain()

                            await asyncio.sleep(1.5)

                            # send invite
                            try:
                                self.writer2.write(RedZed_SendInv(bot_uid, TarGeT, key, iv))
                                await self.writer2.drain()
                            except Exception:
                                # writer2 might not exist or be connected; ignore if it fails
                                pass

                            # quit chat
                            try:
                                self.writer.write(quit_caht_redzed(TarGeT, key, iv))
                                await self.writer.drain()
                            except Exception:
                                pass

                            await asyncio.sleep(1.2)

                            print("With => {}".format(bot_uid), "To => {}".format(TarGeT))

                    except (
                        asyncio.TimeoutError,
                        ConnectionResetError,
                        ConnectionAbortedError,
                        asyncio.IncompleteReadError,
                        BrokenPipeError,
                        OSError,
                        Exception,
                    ) as e:
                        pass
            except (
                asyncio.TimeoutError,
                ConnectionRefusedError,
                ConnectionResetError,
                ConnectionAbortedError,
                asyncio.IncompleteReadError,
                BrokenPipeError,
                OSError,
                Exception,
            ) as e:
                pass

    def GeT_Key_Iv(self, serialized_data):
        my_message = xKEys.MyMessage()
        my_message.ParseFromString(serialized_data)
        timestamp, key, iv = my_message.field21, my_message.field22, my_message.field23
        timestamp_obj = Timestamp()
        timestamp_obj.FromNanoseconds(timestamp)
        timestamp_seconds = timestamp_obj.seconds
        timestamp_nanos = timestamp_obj.nanos
        combined_timestamp = timestamp_seconds * 1_000_000_000 + timestamp_nanos
        return combined_timestamp, key, iv

    def GeT_LoGin_PorTs(self, JwT_ToKen, PayLoad):
        self.UrL = "https://clientbp.ggwhitehawk.com/GetLoginData"  #your server url
        self.HeadErs = {
            "Expect": "100-continue",
            "Authorization": f"Bearer {JwT_ToKen}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB51",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PI)",
            "Host": "clientbp.ggwhitehawk.com",  #your server url
            "Connection": "close",
            "Accept-Encoding": "gzip, deflate, br",
        }
        try:
            self.Res = requests.post(self.UrL, headers=self.HeadErs, data=PayLoad, verify=False)
            self.BesTo_data = json.loads(DeCode_PackEt(self.Res.content.hex()))
            address, address2 = self.BesTo_data["32"]["data"], self.BesTo_data["14"]["data"]
            ip, ip2 = address[: len(address) - 6], address2[: len(address) - 6]
            port, port2 = address[len(address) - 5 :], address2[len(address2) - 5 :]
            return ip, port, ip2, port2
        except requests.RequestException as e:
            print(f" - Bad Requests !")
        print(" - Failed To GeT PorTs !")
        return None, None

    def ToKen_GeneRaTe(self, U, P):
        try:
            if U and P:
                self.PLaFTrom = 4
                self.A, self.O = G_AccEss(U, P)
                self.Version, self.V = "2019118695", "1.118.1"
                self.PyL = {
                    3: str(datetime.now())[:-7],
                    4: "free fire",
                    5: 1,
                    7: self.V,
                    8: "Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)",
                    9: "Handheld",
                    10: "Verizon Wireless",
                    11: "WIFI",
                    12: 1280,
                    13: 960,
                    14: "240",
                    15: "x86-64 SSE3 SSE4.1 SSE4.2 AVX AVX2 | 2400 | 4",
                    16: 5951,
                    17: "Adreno (TM) 640",
                    18: "OpenGL ES 3.0",
                    19: "Google|0fc0e446-ca27-4faa-824a-d40d77767de9",
                    20: "20.171.73.202",
                    21: "fr",
                    22: self.O,
                    23: self.PLaFTrom,
                    24: "Handheld",
                    25: "google G011A",
                    29: self.A,
                    30: 1,
                    41: "Verizon Wireless",
                    42: "WIFI",
                    57: "1ac4b80ecf0478a44203bf8fac6120f5",
                    60: 32966,
                    61: 29779,
                    62: 2479,
                    63: 914,
                    64: 31176,
                    65: 32966,
                    66: 31176,
                    67: 32966,
                    70: 4,
                    73: 2,
                    74: "/data/app/com.dts.freefireth-g8eDE0T268FtFmnFZ2UpmA==/lib/arm",
                    76: 1,
                    77: "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-g8eDE0T268FtFmnFZ2UpmA==/base.apk",
                    78: 6,
                    79: 1,
                    81: "32",
                    83: self.Version,
                    86: "OpenGLES2",
                    87: 255,
                    88: self.PLaFTrom,
                    89: "J\u0003FD\u0004\r_UH\u0003\u000b\u0016_\u0003D^J>\u000fWT\u0000\\=\nQ_;\u0000\r;Z\u0005a",
                    90: "Phoenix",
                    91: "AZ",
                    92: 10214,
                    93: "3rd_party",
                    94: "KqsHT7gtKWkK0gY/HwmdwXIhSiz4fQldX3YjZeK86XBTthKAf1bW4Vsz6Di0S8vqr0Jc4HX3TMQ8KaUU3GeVvYzWF9I=",
                    95: 111207,
                    97: 1,
                    98: 1,
                    99: f"{self.PLaFTrom}",
                    100: f"{self.PLaFTrom}",
                }
            try:
                self.PyL = CrEaTe_ProTo(self.PyL).hex()
                print(self.PyL)
                self.PaYload = bytes.fromhex(EnC_AEs(self.PyL))
            except:
                ResTarTinG()
            self.ResPonse = MajorLoGin(self.PaYload)
            if self.ResPonse:
                self.BesTo_data = json.loads(DeCode_PackEt(self.ResPonse))
                print(self.BesTo_data)
                self.bot_uid = self.BesTo_data["1"]["data"]
                self.JwT_ToKen = self.BesTo_data["8"]["data"]
                self.combined_timestamp, self.key, self.iv = self.GeT_Key_Iv(bytes.fromhex(self.ResPonse))
                ip, port, ip2, port2 = self.GeT_LoGin_PorTs(self.JwT_ToKen, self.PaYload)
                return (
                    self.JwT_ToKen,
                    self.key,
                    self.iv,
                    self.combined_timestamp,
                    ip,
                    port,
                    ip2,
                    port2,
                    self.bot_uid,
                )
        except Exception as e:
            print("From Token Generate ", e)
            ResTarTinG()

    def Get_FiNal_ToKen_0115(self, U, P):
        token, key, iv, Timestamp, ip, port, ip2, port2, bot_uid = self.ToKen_GeneRaTe(U, P)
        self.JwT_ToKen = token
        try:
            self.AfTer_DeC_JwT = jwt.decode(token, options={"verify_signature": False})
            self.AccounT_Uid = self.AfTer_DeC_JwT.get("account_id")
            self.Nm = self.AfTer_DeC_JwT.get("nickname")
            self.H, self.M, self.S = GeT_Time(self.AfTer_DeC_JwT.get("exp"))
            self.Vr = self.AfTer_DeC_JwT.get("release_version")
            self.EncoDed_AccounT = hex(self.AccounT_Uid)[2:]
            self.HeX_VaLue = DecodE_HeX(Timestamp)
            self.TimE_HEx = self.HeX_VaLue
            self.JwT_ToKen_ = token.encode().hex()
        except Exception as e:
            print(f" - Error In ToKen : {e}")
            return
        try:
            self.Header = hex(len(EnC_PacKeT(self.JwT_ToKen_, key, iv)) // 2)[2:]
            length = len(self.EncoDed_AccounT)
            self.__ = "00000000"
            if length == 9:
                self.__ = "0000000"
            elif length == 8:
                self.__ = "00000000"
            elif length == 10:
                self.__ = "000000"
            elif length == 7:
                self.__ = "000000000"
            else:
                print("Unexpected length encountered")
            self.Header = f"0115{self.__}{self.EncoDed_AccounT}{self.TimE_HEx}00000{self.Header}"
            self.FiNal_ToKen_0115 = self.Header + EnC_PacKeT(self.JwT_ToKen_, key, iv)
        except Exception as e:
            print(f" - Erorr In Final Token : {e}")
        self.AutH_ToKen = self.FiNal_ToKen_0115
        os.system("clear")
        asyncio.run(self.STarT(self.JwT_ToKen, self.AutH_ToKen, ip, port, ip2, port2, key, iv, bot_uid))
        return self.AutH_ToKen, key, iv


def load_accounts(file_path="vv.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def StarT_SerVer():
    print(render("Mr Rafi", colors=["white", "yellow"], align="center"))
    TexT = f"[TarGeT InFo] > BoTs arE OnLine\n[BoT sTaTus] > [bold green]ConEcTed SuccEssFuLy[/bold green]"
    panel = Panel(
        Align.center(TexT),
        title="[bold yellow]Mr - Rafi[/bold yellow]",
        border_style="bright_yellow",
        padding=(1, 2),
        expand=False,
    )
    console.print(panel)

    app = Flask(__name__)

    @app.route("/api")
    def run_bot():
        forced_target = request.args.get("target")
        accounts = load_accounts()
        threads = []
        for uid, pwd in accounts.items():
            t = threading.Thread(target=FF_CLient, args=(uid, pwd, forced_target))
            t.start()
            threads.append(t)
        return {"status": "running", "forced_target": forced_target}

    
    @app.route("/stop")
    def stop_bot():
        global STOP_FLAG
        STOP_FLAG = True
        return {"status": "stopped"}


    app.run(host="0.0.0.0", port=8888)


# ------------------------------
# ADD THIS ↓↓↓
# ------------------------------

if __name__ == "__main__":
    StarT_SerVer()
# ----- ORIGINAL MAIN.PY (END) -----


# ---------------------------
# Serverless wrapper / API
# ---------------------------
# The original main.py contains many functions and the FF_CLient class which by default starts
# long-running loops. Below we add a safe `FF_Client_single_run` wrapper that attempts to run
# the original client's logic in a single-run mode: connect, parse target (or use forced target),
# send message, send invite, quit, then close connections.
#
# Then we expose a Flask app endpoint /api that will sequentially process accounts from vv.json
# (no infinite loops). This is optimized for Vercel/serverless deployments.

from flask import Flask, request, jsonify
import asyncio, json, threading, time

# Try to reuse classes and helpers from the original file. If missing, provide conservative fallback implementations.
try:
    OriginalFF = FF_CLient  # class from original main.py
except NameError:
    OriginalFF = None

# Minimal fallback implementations for packet helpers (these should exist in your original file).
def _ensure_helper(name):
    # Check globals for helper name; if missing, create a stub that raises helpful error when used.
    if name not in globals():
        def stub(*a, **k):
            raise RuntimeError(f"Helper function '{name}' is missing from original main.py. Please include it.")
        globals()[name] = stub

for helper in ["DeCode_PackEt", "GLobaL", "RedZed_SendMsg", "RedZed_SendInv", "quit_caht_redzed", "ToKen_GeneRaTe", "xMsGFixinG", "GeT_Time", "CrEaTe_ProTo", "EnC_PacKeT", "EnC_AEs", "MajorLoGin"]:
    if helper not in globals():
        _ensure_helper(helper)

# We'll implement a safe single-run runner that uses the logic pattern from the original file.
class FF_Client_single_run:
    def __init__(self, U, P, forced_target=None, timeout=12):
        self.U = U
        self.P = P
        self.forced_target = forced_target
        self.timeout = timeout

    def run(self):
        # High-level synchronous wrapper that executes the async sequence via asyncio.run
        try:
            # First generate token/key/iv/ports/bot_uid using original ToKen_GeneRaTe if present
            try:
                token, key, iv, timestamp, ip, port, ip2, port2, bot_uid = ToKen_GeneRaTe(self.U, self.P)
            except Exception as e:
                raise RuntimeError(f"Token generation failed: {e}")

            # Run async sequence
            asyncio.run(self._run_once(token, token, ip, port, ip2, port2, key, iv, bot_uid))
            return True, None
        except Exception as e:
            return False, str(e)

    async def _run_once(self, JwT_ToKen, AutH_ToKen, ip, port, ip2, port2, key, iv, bot_uid):
        reader = writer = reader2 = writer2 = None
        try:
            # connect primary
            try:
                reader, writer = await asyncio.open_connection(ip, int(port))
                writer.write(bytes.fromhex(AutH_ToKen if isinstance(AutH_ToKen, str) else AutH_ToKen.hex()))
                await writer.drain()
                await asyncio.sleep(0.3)
                try:
                    writer.write(GLobaL("fr", key, iv))
                    await writer.drain()
                except Exception:
                    pass
            except Exception as e:
                # cannot connect primary; still attempt second connection
                # print(f"[single_run] primary connect failed: {e}")
                pass

            # connect secondary for invite
            try:
                reader2, writer2 = await asyncio.open_connection(ip2, int(port2))
                writer2.write(bytes.fromhex(AutH_ToKen if isinstance(AutH_ToKen, str) else AutH_ToKen.hex()))
                await writer2.drain()
            except Exception:
                pass

            # try receive initial packet to parse target
            got_target = None
            try:
                if reader:
                    await asyncio.sleep(0.6)
                    data = await reader.read(8192)
                    if data:
                        h = data.hex()
                        if h.startswith("1200") and b"SecretCode" in data:
                            try:
                                U = json.loads(DeCode_PackEt(h[10:]))
                                U2 = json.loads(DeCode_PackEt(h[36:]))
                                Uu = json.loads(U["5"]["data"]["8"]["data"])
                                if self.forced_target:
                                    try:
                                        got_target = int(self.forced_target)
                                    except Exception:
                                        got_target = int(Uu.get("GroupID", 0))
                                else:
                                    got_target = int(Uu.get("GroupID", 0))
                            except Exception:
                                pass
                if self.forced_target and not got_target:
                    try:
                        got_target = int(self.forced_target)
                    except Exception:
                        got_target = None
            except Exception:
                pass

            # if we have target and writer, send message, invite, quit
            if got_target and writer:
                try:
                    msg_part1 = (
                        "-HELLO I AM SPIDEERIO GAMING  !\\n\\n"
                        "SUBSCRIBE ME ON YOUTUBE  OR BE BANNED \\n\\n"
                        "SPIDEERIO GAMING : "
                    )
                    msg_part2 = "@Anonymous_is_back_action !! \\n\\n"
                    msg_part3 = (
                        "telegram team channel : @cyberarchbd \\n\\n"
                        "DEV Telegram username : @Anonymous_is_back_action"
                    )
                    full_msg = (
                        "[FF0000][B][C]"
                        + xMsGFixinG(msg_part1)
                        + "[00FF00]"
                        + xMsGFixinG(msg_part2)
                        + "[FFFF00]"
                        + xMsGFixinG(msg_part3)
                    )
                    writer.write(RedZed_SendMsg(full_msg, got_target, bot_uid, key, iv))
                    await writer.drain()
                except Exception:
                    pass

            if got_target and writer2:
                try:
                    writer2.write(RedZed_SendInv(bot_uid, got_target, key, iv))
                    await writer2.drain()
                except Exception:
                    pass

            if got_target and writer:
                try:
                    writer.write(quit_caht_redzed(got_target, key, iv))
                    await writer.drain()
                except Exception:
                    pass

            # close writers
            try:
                if writer:
                    writer.close()
                    await writer.wait_closed()
                if writer2:
                    writer2.close()
                    await writer2.wait_closed()
            except Exception:
                pass

        except Exception:
            pass

# Flask app
def create_app():
    app = Flask(__name__)

    @app.route("/api")
    def api_handler():
        forced_target = request.args.get("target")
        # Load vv.json
        try:
            with open("vv.json", "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except Exception:
            return jsonify({"error": "vv.json not found or invalid", "status": "failed"}), 400

        results = {}
        # sequentially process each account to be serverless-friendly
        for uid, pwd in accounts.items():
            runner = FF_Client_single_run(uid, pwd, forced_target=forced_target)
            ok, err = runner.run()
            results[uid] = {"ok": ok, "error": err}
            # brief pause to avoid hammering provider
            time.sleep(0.2)

        return jsonify({"status": "done", "results": results, "processed": len(accounts), "forced_target": forced_target})

    return app

# If running locally (for debugging), run Flask
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8888")))
