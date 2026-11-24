
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="BEAUTY FINDER",
    page_icon="💄",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #faf8f7;
}
.main-title {
    text-align: center;
    color: #B47B82;
    font-size: 40px;
    font-weight: bold;
}
.sub-title {
    text-align: center;
    color: #888;
    margin-bottom: 30px;
}
.result-box {
    background-color: #F9EEF0;
    padding: 20px;
    border-radius: 12px;
    color: #965B68;
}
.best-box {
    background-color: #FFF4E6;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #EDDDC7;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 상품 데이터 (테스트용 가상 데이터)
# -----------------------------

products = {
    "파우더": [
        {
            "name": "A 파우더",
            "brand": "브랜드 A",
            "price": 12000,
            "amount": "10g",
            "color": "투명",
            "review": "가벼운 사용감과 보송한 마무리가 장점",
            "quality": 95,
            "trend": 85,
            "budget": 90
        },
        {
            "name": "B 파우더",
            "brand": "브랜드 B",
            "price": 9000,
            "amount": "9g",
            "color": "내추럴",
            "review": "가격 대비 품질과 유분 조절력이 좋다는 평가",
            "quality": 88,
            "trend": 96,
            "budget": 98
        },
        {
            "name": "C 파우더",
            "brand": "브랜드 C",
            "price": 15000,
            "amount": "12g",
            "color": "라벤더",
            "review": "밀착력과 지속력이 우수하다는 평가",
            "quality": 92,
            "trend": 90,
            "budget": 82
        }
    ],
    "팩트": [
        {
            "name": "A 팩트",
            "brand": "브랜드 A",
            "price": 18000,
            "amount": "12g",
            "color": "21호",
            "review": "자연스러운 피부 표현과 커버력이 장점",
            "quality": 96,
            "trend": 90,
            "budget": 85
        },
        {
            "name": "B 팩트",
            "brand": "브랜드 B",
            "price": 13000,
            "amount": "10g",
            "color": "23호",
            "review": "휴대성이 좋고 가성비가 뛰어남",
            "quality": 86,
            "trend": 88,
            "budget": 98
        },
        {
            "name": "C 팩트",
            "brand": "브랜드 C",
            "price": 22000,
            "amount": "15g",
            "color": "21호",
            "review": "밀착력과 지속력이 좋다는 평가",
            "quality": 94,
            "trend": 97,
            "budget": 80
        }
    ],
    "쿠션": [
        {
            "name": "A 쿠션",
            "brand": "브랜드 A",
            "price": 25000,
            "amount": "15g",
            "color": "21호",
            "review": "커버력과 밀착력이 좋다는 평가",
            "quality": 96,
            "trend": 90,
            "budget": 88
        },
        {
            "name": "B 쿠션",
            "brand": "브랜드 B",
            "price": 19000,
            "amount": "13g",
            "color": "23호",
            "review": "촉촉한 발림성과 자연스러운 광채",
            "quality": 89,
            "trend": 96,
            "budget": 95
        },
        {
            "name": "C 쿠션",
            "brand": "브랜드 C",
            "price": 28000,
            "amount": "15g",
            "color": "21호",
            "review": "지속력과 피부 밀착력이 우수함",
            "quality": 95,
            "trend": 98,
            "budget": 82
        }
    ],
    "립스틱": [
        {
            "name": "A 립스틱",
            "brand": "브랜드 A",
            "price": 15000,
            "amount": "3.5g",
            "color": "로즈",
            "review": "발색력이 선명하고 발림성이 좋음",
            "quality": 95,
            "trend": 90,
            "budget": 90
        },
        {
            "name": "B 립스틱",
            "brand": "브랜드 B",
            "price": 11000,
            "amount": "3g",
            "color": "코랄",
            "review": "촉촉하고 자연스러운 색감이 장점",
            "quality": 88,
            "trend": 94,
            "budget": 98
        },
        {
            "name": "C 립스틱",
            "brand": "브랜드 C",
            "price": 20000,
            "amount": "3.5g",
            "color": "누드",
            "review": "색상 지속력이 좋다는 평가",
            "quality": 93,
            "trend": 98,
            "budget": 82
        }
    ]
}

# -----------------------------
# 제목
# -----------------------------

st.markdown(
    '<div class="main-title">BEAUTY FINDER</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'AI BEAUTY PRODUCT RECOMMENDATION'
    '<br>나에게 맞는 화장품 찾기'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# STEP 1. 우선순위
# -----------------------------

st.subheader("STEP 1. 우선순위를 선택하세요.")

priority = st.radio(
    "우선순위",
    ["예산맞춤", "유행", "제품성"],
    horizontal=True
)

# -----------------------------
# STEP 2. 카테고리
# -----------------------------

st.subheader("STEP 2. 화장품 카테고리를 선택하세요.")

category_option = st.radio(
    "카테고리",
    ["파우더", "팩트", "쿠션", "립스틱", "직접 입력"],
    horizontal=True
)

if category_option == "직접 입력":
    category = st.text_input(
        "화장품 카테고리 입력",
        placeholder="예: 블러셔, 아이섀도우"
    )
else:
    category = category_option

# -----------------------------
# STEP 3. 예산
# -----------------------------

st.subheader("STEP 3. 예산 설정")

budget = st.radio(
    "예산 범위",
    ["전체 가격", "1만원 이하", "1~2만원", "2~3만원"],
    horizontal=True
)

# -----------------------------
# 분석하기
# -----------------------------

if st.button("✨ 분석하기", use_container_width=True):

    if not category.strip():
        st.warning("화장품 카테고리를 입력해주세요.")

    elif category not in products:
        st.warning(
            "현재 해당 카테고리의 테스트 상품 데이터가 없습니다."
        )

    else:
        result = products[category].copy()

        if budget == "1만원 이하":
            result = [p for p in result if p["price"] <= 10000]

        elif budget == "1~2만원":
            result = [
                p for p in result
                if 10000 <= p["price"] <= 20000
            ]

        elif budget == "2~3만원":
            result = [
                p for p in result
                if 20000 <= p["price"] <= 30000
            ]

        if not result:
            st.warning("해당 예산에 맞는 제품이 없습니다.")

        else:
            score_key = {
                "예산맞춤": "budget",
                "유행": "trend",
                "제품성": "quality"
            }

            result.sort(
                key=lambda p: p[score_key[priority]],
                reverse=True
            )

            st.session_state["result"] = result
            st.session_state["priority"] = priority
            st.session_state["category"] = category

# -----------------------------
# 분석 결과
# -----------------------------

if "result" in st.session_state:

    result = st.session_state["result"]
    priority = st.session_state["priority"]
    category = st.session_state["category"]

    st.divider()
    st.subheader("STEP 4. AI 분석 결과")

    messages = {
        "예산맞춤": "예산과 가성비를 고려한 추천 목록입니다.",
        "유행": "인기와 유행을 고려한 추천 목록입니다.",
        "제품성": "제품성을 고려한 추천 목록입니다."
    }

    st.markdown(
        f'<div class="result-box">'
        f'<h3>{messages[priority]}</h3>'
        f'<p>검색 카테고리: {category}</p>'
        f'</div>',
        unsafe_allow_html=True
    )

    st.subheader("추천 제품 TOP 3")

    table_data = []

    for p in result:
        table_data.append({
            "제품명": p["name"],
            "브랜드": p["brand"],
            "가격": f'{p["price"]:,}원',
            "실제 후기 요약 예시": p["review"],
            "용량": p["amount"],
            "색상": p["color"]
        })

    st.table(pd.DataFrame(table_data))

    # -------------------------
    # 최종 추천
    # -------------------------

    best = result[0]

    st.divider()

    st.markdown(
        '<div class="best-box">',
        unsafe_allow_html=True
    )

    st.subheader("🏆 최종 BEST 추천 제품")

    st.title(best["name"])

    st.write(f"브랜드: {best['brand']}")
    st.write(f"가격: {best['price']:,}원")
    st.write(f"용량: {best['amount']}")
    st.write(f"색상: {best['color']}")

    st.markdown("### 💡 추천 이유")

    reasons = {
        "예산맞춤":
            "가격과 용량 대비 가성비가 가장 우수합니다. "
            "예산 조건을 고려했을 때 합리적인 선택입니다.",

        "유행":
            "인기와 트렌드 점수가 가장 높습니다. "
            "소비자 선호도를 고려했을 때 추천하는 제품입니다.",

        "제품성":
            "제품성 평가 점수가 가장 높습니다. "
            "사용감과 품질을 고려했을 때 가장 적합한 제품입니다."
    }

    st.write(reasons[priority])
    st.write(f"후기 참고: {best['review']}")

    st.markdown('</div>', unsafe_allow_html=True)

    st.caption(
        "※ 현재 상품명과 후기는 테스트용 가상 데이터입니다."
    )

st.divider()
st.caption("BEAUTY FINDER | AI BEAUTY RECOMMENDATION")
