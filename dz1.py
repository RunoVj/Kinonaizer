import random
import sys


def get_res_for_first_win():
    first_tm_scored_goal = random.randint(2, 4)
    second_tm_scored_goal = random.randint(0, 1)
    # num win/num lose/num draw/scored a goal/missed a goal/score
    first_tm_res = [1, 0, 0, first_tm_scored_goal, second_tm_scored_goal, 3]
    second_tm_res = [0, 1, 0, second_tm_scored_goal, first_tm_scored_goal, 0]
    return first_tm_res, second_tm_res


def get_res_for_second_win():
    first_tm_scored_goal = random.randint(0, 1)
    second_tm_scored_goal = random.randint(2, 4)
    # num win/num lose/num draw/scored a goal/missed a goal/score
    first_tm_res = [0, 1, 0, first_tm_scored_goal, second_tm_scored_goal, 0]
    second_tm_res = [1, 0, 0, second_tm_scored_goal, first_tm_scored_goal, 3]
    return first_tm_res, second_tm_res


def get_res_for_draw():
    total_goals = random.randint(0, 2)
    # num win/num lose/num draw/scored a goal/missed a goal/score
    first_tm_res = [0, 0, 1, total_goals, total_goals, 1]
    second_tm_res = [0, 0, 1, total_goals, total_goals, 1]
    return first_tm_res, second_tm_res


def update_table_of_each_match(table_of_each_match_func, team_first, team_second, res_for_first, res_for_second):
    concat_f_and_s = team_first + ' - ' + team_second
    concat_s_and_f = team_second + ' - ' + team_first

    check_concat_first = table_of_each_match_func.get(concat_f_and_s)
    check_concat_second = table_of_each_match_func.get(concat_s_and_f)

    if check_concat_first in table_of_each_match_func or check_concat_second in table_of_each_match_func:
        print("ERROR")
        return None
    else:
        table_of_each_match_func[concat_f_and_s] = [res_for_first[4], res_for_second[4]]
        table_of_each_match_func[concat_s_and_f] = [res_for_second[4], res_for_first[4]]


def update_result_of_championship(table_of_championship_func, team, result_match):
    check_team = table_of_championship_func.get(team)
    if check_team is not None:
        for i in range(6):
            table_of_championship_func[team][i] += result_match[i]
    else:
        print("ERROR; team = ", team)


def update_table_of_championship(table_of_championship_func, table_of_each_match_func, team_first, team_second,
                                 code_res_for_first_team):
    first_tm_cur = table_of_championship_func.get(team_first)
    second_tm_cur = table_of_championship_func.get(team_second)

    if first_tm_cur is not None and second_tm_cur is not None:
        if code_res_for_first_team is 0:
            res_for_first_tm, res_for_second_tm = get_res_for_first_win()

        elif code_res_for_first_team is 1:
            res_for_first_tm, res_for_second_tm = get_res_for_second_win()

        elif code_res_for_first_team is 2:
            res_for_first_tm, res_for_second_tm = get_res_for_draw()

        else:
            print("ERROR, code_res_for_first_team = ", code_res_for_first_team)
            return None

        update_result_of_championship(table_of_championship_func, team_first, res_for_first_tm)
        update_result_of_championship(table_of_championship_func, team_second, res_for_second_tm)

        update_table_of_each_match(table_of_each_match_func, team_first, team_second, res_for_first_tm,
                                   res_for_second_tm)

    else:
        print("Error first or second team")
        return None


def print_result_team(table_of_championship_func, team):
    result = table_of_championship_func.get(team)
    if result is not None:
        for i in result:
            print(i, ' ; ', end='')
        print('')
    else:
        print("ERROR TEAM ", team)
        return None


def print_championship_table(table):
    if len(table) is 0:
        print("Empty table of championship")
        return None

    sort_list_team = list()

    for cnt in range(len(table)):

        max_score = 0
        team_of_max_score = ''

        for team, result in table.items():
            if result[5] > max_score and team not in sort_list_team:
                max_score = result[5]
                team_of_max_score = team

        sort_list_team += [team_of_max_score]

        print(cnt + 1, ". ", team_of_max_score, ": ", end="")
        print_result_team(table, team_of_max_score)


def get_result_of_match(table_of_championship_func, team_first, team_second):
    if len(table_of_championship_func) is 0:
        print("table of championship is empty")
        return None
    else:
        concat_f_and_s = team_first + ' - ' + team_second
        return table_of_championship_func.get(concat_f_and_s)


def print_match(table_of_championship_func, team_first, team_second):
    res_of_match = get_result_of_match(table_of_championship_func, team_first, team_second)
    if res_of_match is not None:
        print(team_first, "-", team_second, " ", res_of_match[0], " : ", res_of_match[1])
    else:
        print("ERROR INPUT TEAM")
        return None
    return True


if __name__ == "__main__":

    team_list = ['Лейкерс', 'ЦСКА', 'Майами', 'Бостон', 'Чикаго', 'Кливленд', 'Уникс', 'Бруклин']

    table_of_each_match = dict()
    table_of_championship = dict()

    for i in range(len(team_list) - 1):
        for j in range(i + 1, len(team_list)):

            # num win/num lose/num draw/scored a goal/missed a goal/score
            if team_list[i] not in table_of_championship:
                table_of_championship[team_list[i]] = [0] * 6
            if team_list[j] not in table_of_championship:
                table_of_championship[team_list[j]] = [0] * 6

            result_match_code = random.randint(0, 2)  # 0 - i win, 1 - i lose, 2 - draw

            update_table_of_championship(table_of_championship, table_of_each_match, team_list[i], team_list[j],
                                         result_match_code)

    print_championship_table(table_of_championship)

    if len(sys.argv) is not 3:
        print("Bad input argument. Please, enter the three arguments")
        print("You input ", len(sys.argv), " arguments")
    else:
        check_err = print_match(table_of_each_match, sys.argv[1], sys.argv[2])
        if check_err is None:
            print("Example team: ", team_list)
