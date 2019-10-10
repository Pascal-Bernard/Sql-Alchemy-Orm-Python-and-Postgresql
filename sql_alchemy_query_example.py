# Let's say we want to fetch the following key from the JSON Blob:

# Table name: `table`
# ------------------------------------------------------------
# id     item_id   created_at   json_data 
# 1    | 12345  | 2019-01-01 | [{"jsonId": 1},{"data": "abc"}] 
# 2    | 23456  | 2019-01-02 | [{"jsonId": 2},{"data": "bcd"}] 
# 3    | 34567  | 2019-01-03 | [{"jsonId": 3},{"data": "cde"}] 
# 4    | 45678  | 2019-01-04 | [{"jsonId": 4},{"data": "efg"}] 
# 5    | 56789  | 2019-01-05 | [{"jsonId": 5},{"data": "fgh"}] 
# 6    | 67890  | 2019-01-06 | [{"jsonId": 6},{"data": "ghi"}] 

rows = session.query(Loans).filter(
    Table.json_data.contains([
        {"type": "A"}
        ])
    ).order_by(Table.id.desc()).limit(5).all()
 
for row in rows:
    print(user.loan_json_data[0].get('jsonId'))

# output

1
2
3
4
5
