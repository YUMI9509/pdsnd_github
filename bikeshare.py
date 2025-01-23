import time
import pandas as pd
import numpy as np

# 도시 이름과 데이터 파일 경로를 매핑
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    사용자로부터 분석할 도시, 월, 요일을 입력받아 반환합니다.
    """
    print('안녕하세요! 미국 자전거 공유 데이터를 탐색해봅시다!')

    city = input_valid("분석할 도시 이름을 입력하세요", list(CITY_DATA.keys()))
    month = input_valid("필터링할 월을 입력하세요 ('all', 'january' ... 'december')",
                        ['all', 'january', 'february', 'march', 'april', 'may', 'june',
                         'july', 'august', 'september', 'october', 'november', 'december'])
    day = input_valid("필터링할 요일을 입력하세요 ('all', 'monday' ... 'sunday')",
                      ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])

    print(f"\n입력한 값 - 도시: '{city}', 월: '{month}', 요일: '{day}'")
    print('-' * 40)
    return city, month, day

def input_valid(prompt, valid_options):
    """
    사용자가 유효한 값을 입력할 때까지 반복해서 입력받습니다.
    """
    while True:
        user_input = input(f"{prompt} {valid_options}: ").lower()
        if user_input in valid_options:
            return user_input
        print("잘못된 입력입니다. 다시 입력해주세요.")

def load_data(city, month, day):
    """
    지정된 도시 데이터를 불러오고 월과 요일로 필터링합니다.
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.strftime('%B').str.lower()
    df['Day'] = df['Start Time'].dt.day_name().str.lower()

    if month != 'all':
        df = df[df['Month'] == month]
    if day != 'all':
        df = df[df['Day'] == day]

    return df

def time_stats(df):
    """
    가장 빈번한 월, 요일, 시간을 출력합니다.
    """
    print('\n가장 빈번한 여행 시간 통계를 계산 중입니다...\n')
    start_time = time.time()

    print(f"가장 흔한 월: {df['Month'].mode()[0]}")
    print(f"가장 흔한 요일: {df['Day'].mode()[0]}")
    df['Hour'] = df['Start Time'].dt.hour
    print(f"가장 흔한 시간: {df['Hour'].mode()[0]}시")

    print(f"\n이 통계를 계산하는 데 {time.time() - start_time:.4f}초가 걸렸습니다.")
    print('-' * 40)

def station_stats(df):
    """
    가장 인기 있는 출발지, 도착지 및 경로를 출력합니다.
    """
    print('\n가장 인기 있는 역 통계를 계산 중입니다...\n')
    start_time = time.time()

    print(f"가장 많이 사용된 출발지: {df['Start Station'].mode()[0]}")
    print(f"가장 많이 사용된 도착지: {df['End Station'].mode()[0]}")
    route = (df['Start Station'] + " -> " + df['End Station']).mode()[0]
    print(f"가장 빈번한 경로: {route}")

    print(f"\n이 통계를 계산하는 데 {time.time() - start_time:.4f}초가 걸렸습니다.")
    print('-' * 40)

def trip_duration_stats(df):
    """
    총 여행 시간과 평균 여행 시간을 출력합니다.
    """
    print('\n여행 시간 통계를 계산 중입니다...\n')
    start_time = time.time()

    total_time = df['Trip Duration'].sum()
    mean_time = df['Trip Duration'].mean()
    print(f"총 여행 시간: {format_time(total_time)}")
    print(f"평균 여행 시간: {format_time(mean_time)}")

    print(f"\n이 통계를 계산하는 데 {time.time() - start_time:.4f}초가 걸렸습니다.")
    print('-' * 40)

def format_time(seconds):
    """
    초 단위의 시간을 시, 분, 초로 변환하여 반환합니다.
    """
    hours = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = round(seconds % 60, 2)
    return f"{hours}시간 {mins}분 {secs}초"

def user_stats(df):
    """
    사용자 유형, 성별, 출생 연도 통계를 출력합니다.
    """
    print('\n사용자 통계를 계산 중입니다...\n')
    start_time = time.time()

    print("사용자 유형별 개수:")
    print(df['User Type'].value_counts(), "\n")

    if 'Gender' in df.columns:
        print("성별별 개수:")
        print(df['Gender'].value_counts(), "\n")
    else:
        print("성별 데이터가 없습니다.")

    if 'Birth Year' in df.columns:
        print(f"가장 오래된 출생 연도: {int(df['Birth Year'].min())}")
        print(f"가장 최근 출생 연도: {int(df['Birth Year'].max())}")
        print(f"가장 흔한 출생 연도: {int(df['Birth Year'].mode()[0])}")
    else:
        print("출생 연도 데이터가 없습니다.")

    print(f"\n이 통계를 계산하는 데 {time.time() - start_time:.4f}초가 걸렸습니다.")
    print('-' * 40)

def display_raw_data(df):
    """
    원시 데이터를 5행씩 사용자에게 출력합니다.
    """
    start_row = 0
    while True:
        show_data = input("\n원시 데이터를 5행씩 더 보고 싶으신가요? 'yes' 또는 'no'로 입력하세요: ").lower()
        if show_data == 'yes':
            print(df.iloc[start_row:start_row + 5])
            start_row += 5
            if start_row >= len(df):
                print("\n더 이상 표시할 데이터가 없습니다.")
                break
        elif show_data == 'no':
            break
        else:
            print("잘못된 입력입니다. 'yes' 또는 'no'로 입력해주세요.")

def main():
    """
    프로그램의 메인 실행 루프.
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df.empty:
            print("입력한 조건에 맞는 데이터가 없습니다.")
        else:
            display_raw_data(df)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        restart = input('\n다시 시작하시겠습니까? "yes" 또는 "no"를 입력하세요.\n').lower()
        if restart != 'yes':
            print("프로그램을 종료합니다. 감사합니다!")
            break

if __name__ == "__main__":
    main()
