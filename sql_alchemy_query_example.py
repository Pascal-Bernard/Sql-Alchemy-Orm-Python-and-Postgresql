# Let's say we want to fetch the following key from the JSON Blob:
# Table name: `table`
# ------------------------------------------------------------
#   id     item_id  created_at   json_data 
# | 1    | 12345  | 2019-01-01 | [{"jsonId": 1}, {"type": "A"}, {"data": "abc"}] 
# | 2    | 23456  | 2019-01-02 | [{"jsonId": 2}, {"type": "A"}, {"data": "bcd"}] 
# | 3    | 34567  | 2019-01-03 | [{"jsonId": 3}, {"type": "A"}, {"data": "cde"}] 
# | 4    | 45678  | 2019-01-04 | [{"jsonId": 4}, {"type": "A"}, {"data": "efg"}] 
# | 5    | 56789  | 2019-01-05 | [{"jsonId": 5}, {"type": "A"}, {"data": "fgh"}] 
# | 6    | 67890  | 2019-01-06 | [{"jsonId": 6}, {"type": "B"}, {"data": "ghi"}] 

rows = session.query(Table).filter(
    Table.json_data.contains([
        {"type": "A"}
        ])
    ).order_by(Table.id.desc()).limit(3).all()
 
for row in rows:
    print(row.json_data[0].get('jsonId'))

# output
1
2
3
