#!/usr/bin/python3

import re
                
def calc(A, B):
    # バグ2の修正: 入力が整数かどうかをチェック
    # isinstanceで型を確認し、int以外なら -1 を返す
    if not isinstance(A, int) or not isinstance(B, int):
        return -1
        
    # バグ1の修正: 範囲チェックの条件を正しく設定
    # 1未満、または999より大きい場合は -1 を返す
    if A < 1 or A > 999 or B < 1 or B > 999:
        return -1
        
    # 条件を満たす場合のみ計算
    return A * B
    
def main ():
	match = False
	print ("input A: ")
	A = input ()
	print ("input B: ")
	B = input ()
	print ("input C: ")
	C = calc(A, B)
	print ("C = " + str(C))

if __name__ == '__main__':
	main()
