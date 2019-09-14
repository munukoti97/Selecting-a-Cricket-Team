from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error



app = Flask(__name__)


@app.route('/')
def index():
        return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    name_location =request.form['location']
    name_match = request.form['match']
    name_opp=request.form['opp']
    try:
        mySQLconnection = mysql.connector.connect(host='127.0.0.1',
                                                  database='cricket',
                                                  user='root',
                                                  password='Harshal#1',auth_plugin='mysql_native_password')
        getchar =name_match

        if getchar == "t_20":
            sql_select_Query = "select * from t_20_batsman"
            sql_select_Query1 = "select MAX(TOTAL_RUNS) from t_20_batsman"
            sql_select_Query2 = "select * from cric_main"
            sql_select_Query3 = "select * from t_20_bowler"
            sql_select_Query4 = "select * from t_20_allrounder"
            sql_select_Query5 = "select MAX(WICKETS) from t_20_bowler"
            sql_select_Query6 = "select MAX(DOT_BALL) from t_20_bowler"
            sql_select_Query7 = "select MAX(TOTAL_RUNS) from t_20_allrounder"
            sql_select_Query8 = "select MAX(WICKETS) from t_20_allrounder"
            sql_select_Query9 = "select MAX(DOT_BALL) from t_20_allrounder"
            sql_select_Query10 = "select "+name_location+" from location "
            sql_select_Query11 = "select "+name_opp+" from opponent "
            
        else:
            if getchar == "odi":
                sql_select_Query = "select * from odi_batsman"
                sql_select_Query1 = "select MAX(TOTAL_RUNS) from odi_batsman"
                sql_select_Query2 = "select * from cric_main"
                sql_select_Query3 = "select * from odi_bowler"
                sql_select_Query4 = "select * from odi_allrounder"
                sql_select_Query5 = "select MAX(WICKETS) from odi_bowler"
                sql_select_Query6 = "select MAX(DOT_BALL) from odi_bowler"
                sql_select_Query7 = "select MAX(TOTAL_RUNS) from odi_allrounder"
                sql_select_Query8 = "select MAX(WICKETS) from odi_allrounder"
                sql_select_Query9 = "select MAX(DOT_BALL) from odi_allrounder"
                sql_select_Query10 = "select "+name_location+" from location"
                sql_select_Query11 = "select "+name_opp+" from opponent "
                
            else:
                sql_select_Query = "select * from test_batsman"
                sql_select_Query1 = "select MAX(TOTAL_RUNS) from test_batsman"
                sql_select_Query2 = "select * from cric_main"
                sql_select_Query3 = "select * from test_bowler"
                sql_select_Query4 = "select * from test_allrounder"
                sql_select_Query5 = "select MAX(WICKETS) from test_bowler"
                sql_select_Query6 = "select MAX(DOT_BALL) from test_bowler"
                sql_select_Query7 = "select MAX(TOTAL_RUNS) from test_allrounder"
                sql_select_Query8 = "select MAX(WICKETS) from test_allrounder"
                sql_select_Query9 = "select MAX(DOT_BALL) from test_allrounder"
                sql_select_Query10 = "select "+name_location+" from location"
                sql_select_Query11 = "select "+name_opp+" from opponent "
        print(name_location)
        cursor = mySQLconnection.cursor()

        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        cursor.execute(sql_select_Query1)
        records1 = cursor.fetchall()

        cursor.execute(sql_select_Query2)
        records2 = cursor.fetchall()

        cursor.execute(sql_select_Query3)
        records3 = cursor.fetchall()

        cursor.execute(sql_select_Query4)
        records4 = cursor.fetchall()

        cursor.execute(sql_select_Query5)
        records5 = cursor.fetchall()

        cursor.execute(sql_select_Query6)
        records6 = cursor.fetchall()

        cursor.execute(sql_select_Query7)
        records7 = cursor.fetchall()

        cursor.execute(sql_select_Query8)
        records8 = cursor.fetchall()

        cursor.execute(sql_select_Query9)
        records9 = cursor.fetchall()

        cursor.execute(sql_select_Query10)
        records10 = cursor.fetchall()

        cursor.execute(sql_select_Query11)
        records11 = cursor.fetchall()

        y = records1[0]
        print(y[0])

        d = records5[0]

        e = records6[0]

        f = records7[0]

        g = records8[0]

        h = records9[0]

        pitch = records10[0]

        
        
        s = int(pitch[0])
        print(pitch[0])

        i = 0
        j = 0
        a = []
        a.append([0] * 30)
        a.append([1] * 30)
        a.append([2] * 30)

        b = []
        b.append([0] * 30)
        b.append([1] * 30)

        c = []
        c.append([0] * 30)
        c.append([1] * 30)

        print("Total number of rows in python_developers is - ", cursor.rowcount)
        print("Printing each row's column values i.e.  developer record")

        for row in records:
            x = records2[i]
            opp=records10[i]
            i = i + 1
            if (x[5] == "yes" and (getchar == "t_20" ) and (x[6]>=18 and x[6]<=32)):
                st = (row[1] / 600) * 15
                hc = (row[2] / row[4]) * 10
                tr = (row[3] / y[0]) * 10
                ft = x[3]
                pitch = records10[i]
                sum = st + hc + tr + ft + int(pitch[0])+opp[0]
                a[0][j] = row[0]
                a[1][j] = sum
                a[2][j] = x[1]
                j = j + 1
            if (x[5] == "yes" and (getchar == "test") and (x[6]>=25 and x[6]<=45)):
                st = (row[1] / 600) * 5
                fc = (row[2] / row[4]) * 15
                tr = (row[3] / y[0]) * 10
                ft = x[3]
                pitch = records10[i]
                sum = st + fc + tr + ft + int(pitch[0])+opp[0]
                a[0][j] = row[0]
                a[1][j] = sum
                a[2][j] = x[1]
                j = j + 1
            if (x[5] == "yes" and (getchar == "odi") and (x[6]>=25 and x[6]<=40)):
                st = (row[1] / 600) * 10
                fc = (row[2] / row[4]) * 10
                tr = (row[3] / y[0]) * 10
                ft = x[3]
                pitch = records10[i]
                sum = st + fc + tr + ft + int(pitch[0])+opp[0]
                a[0][j] = row[0]
                a[1][j] = sum
                a[2][j] = x[1]
                j = j + 1


        o = 0

        while o < 5:
            u = o + 1
            while u < j:
                if a[1][o] < a[1][u]:
                    temp = a[1][o]
                    a[1][o] = a[1][u]
                    a[1][u] = temp
                    temp1 = a[2][o]
                    a[2][o] = a[2][u]
                    a[2][u] = temp1
                u = u + 1
            o = o + 1
        j = 0
        r = 0
        while r < 5:
            print(" {} and {}".format(a[2][r], a[1][r]))

            r = r + 1
        r = 0
        for row in records3:
            x = records2[i]
            pitch = records10[i]
            opp=records10[i]
            i = i + 1
            if (x[5] == "yes" and (getchar == "t_20" ) and (x[6]>=18 and x[6]<=35)):
                er = 10 - ((row[1] / 36) * 10)
                nw = (row[2] / d[0]) * 10
                db = (row[3] / e[0]) * 10
                ft = x[3]
                sum = er + nw + db + ft + int(pitch[0])+opp[0]
                b[0][j] = x[1]
                b[1][j] = sum
                j = j + 1
            if (x[5] == "yes" and (getchar == "odi") and (x[6]>=20 and x[6]<=40)):
                er = 10 - ((row[1] / 36) * 10)
                nw = (row[2] / d[0]) * 10
                db = (row[3] / e[0]) * 10
                ft = x[3]
                sum = er + nw + db + ft + int(pitch[0])+opp[0]
                b[0][j] = x[1]
                b[1][j] = sum
                j = j + 1
            if (x[5] == "yes" and (getchar == "test") and (x[6]>=25 and x[6]<=45)):
                er = 10 - ((row[1] / 36) * 10)
                nw = (row[2] / d[0]) * 10
                db = (row[3] / e[0]) * 10
                ft = x[3]
                sum = er + nw + db + ft + int(pitch[0])+opp[0]
                b[0][j] = x[1]
                b[1][j] = sum
                j = j + 1
        o = 0
        while o < 5:
            u = o + 1
            while u < j:
                if b[1][o] < b[1][u]:
                    temp = b[1][o]
                    b[1][o] = b[1][u]
                    b[1][u] = temp
                    temp = b[0][o]
                    b[0][o] = b[0][u]
                    b[0][u] = temp
                u = u + 1
            o = o + 1
        j = 0
        while r < 5:
            print(" {} and {}".format(b[0][r], b[1][r]))
            r = r + 1
        r = 0
        for row in records4:
            x = records2[i]
            pitch = records10[i]
            opp=records10[i]
            i = i + 1
            if (x[5] == "yes" and (getchar == "t_20" )and (x[6]>=18 and x[6]<=35)):
                st = (row[1] / 600) * 15

                hc = (row[2] / row[7]) * 10

                tr = (row[3] / f[0]) * 10
                er = 10 - ((row[4] / 36) * 10)
                nw = (row[5] / g[0]) * 10
                db = (row[6] / h[0]) * 10

                ft = x[3]
                sum = er + nw + db + ft + st + hc + tr + int(pitch[0])+opp[0]
                c[0][j] = x[1]
                c[1][j] = sum
                j = j + 1
            if (x[5] == "yes" and (getchar == "odi")and (x[6]>= 20 and x[6]<=40)):
                st = (row[1] / 600) * 10

                hc = (row[2] / row[7]) * 10

                tr = (row[3] / f[0]) * 10
                er = 10 - ((row[4] / 36) * 10)
                nw = (row[5] / g[0]) * 10
                db = (row[6] / h[0]) * 10

                ft = x[3]
                sum = er + nw + db + ft + st + hc + tr + int(pitch[0])+opp[0]
                c[0][j] = x[1]
                c[1][j] = sum
                j = j + 1
            if (x[5] == "yes" and (getchar == "test") and  (x[6]>=25 and x[6]<=40)):
                st = (row[1] / 600) * 5
                hc = (row[2] / row[7]) * 15
                tr = (row[3] / f[0]) * 10
                er = 10 - ((row[4] / 36) * 10)
                nw = (row[5] / g[0]) * 10
                db = (row[6] / h[0]) * 10
                ft = x[3]
                sum = er + nw + db + ft + st + hc + tr + int(pitch[0])+opp[0]
                c[0][j] = x[1]
                c[1][j] = sum
                j = j + 1
        o = 0
        while o < 5:
            u = o + 1
            while u < j:
                if c[1][o] < c[1][u]:
                    temp = c[1][o]
                    c[1][o] = c[1][u]
                    c[1][u] = temp
                    temp = c[0][o]
                    c[0][o] = c[0][u]
                    c[0][u] = temp
                u = u + 1
            o = o + 1
        while r < 5:
            print(" {} and {}".format(c[0][r], c[1][r]))
            r = r + 1
        r = 0
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if (mySQLconnection.is_connected()):
            mySQLconnection.close()
            print("MySQL connection is closed")

    return render_template("pass.html", n1=a[2][0],n2=a[2][1],n3=a[2][2],n4=a[2][3],n5=a[2][4],n6=b[0][0],n7=b[0][1],n8=b[0][2],n9=b[0][3],n10=b[0][4],n11=c[0][0],n12=c[0][1],n13=c[0][2],n14=c[0][3],n15=c[0][4])


if __name__ == '__main__':
    app.run(debug=True)
