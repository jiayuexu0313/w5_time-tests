import times
import datetime

def test_given_input():
    # 创建测试输入
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    # 计算重叠时间
    result = times.compute_overlap_time(large, short)

    # 期望的结果
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
    ]

    # 使用 datetime 解析字符串
    def parse_time_ranges(time_ranges):
        return [
            (datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S"), 
             datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S"))
            for start, end in time_ranges
        ]

    # 将结果和期望值都解析为 datetime 对象
    parsed_result = parse_time_ranges(result)
    parsed_expected = parse_time_ranges(expected)

    # 使用断言检查结果是否和期望一致，允许几秒的误差
    for (start_r, end_r), (start_e, end_e) in zip(parsed_result, parsed_expected):
        assert abs((start_r - start_e).total_seconds()) < 60, f"Start times do not match: {start_r} vs {start_e}"
        assert abs((end_r - end_e).total_seconds()) < 60, f"End times do not match: {end_r} vs {end_e}"

if __name__ == "__main__":
    test_given_input()
    print("Test passed!")
