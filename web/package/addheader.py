def addhead(tier, df_html):
    fullhtml = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>This is your winrate...</title>  
</head>
<body>
    <h2>최근 경기 중 최대 20개를 분석하여 해당 경기의 승률을 알려줍니다.</h2>
    <p>자신의 kda, cs, object, 그리고 나의 팀의 kd을 이용해 승률을 분석합니다.
        <br>실제 경기의 승패여부와 모델이 예측한 승패여부를 비교해보세요.
    </p>
    <h3>현재 티어: <b>{tier}</b> </h3>
    {df_html}
    <p> * <b>위</b>는 <b>자신의 전적만으로</b> 승률을 예측한 모델의 표입니다. </p>
    <p> * <b>아래</b>는 나의 전적과 <b>아군 팀의 전체 kill, death까지</b> 포함해 승률을 예측한 모델의 표입니다. </p>
    <p> * <b>승률 50%에 근접</b>한 박빙의 승부에는 <b>예측이 부정확</b>할 수 있습니다. ^^; </p>
    <form action="/main" method="get">
    <button>Back</button>
    </form>
</body>
</html>
"""
    return fullhtml