#-*-coding:utf-8-*-
import module.mKLT as KLT
kr = "인생은 가까이서 보면 비극이지만 멀리서 보면 희극이다."

if __name__ == '__main__':
    # -- 한글 MOP

    # -- KLT : PoS-Tagging
    print('KLT 형태소 분석 :')
    print(KLT.pos(kr)) # 형태소+빈도 수 추출

    print('KLT 명사 추출 : ')
    print(KLT.nouns(kr)) # 명사 추출
