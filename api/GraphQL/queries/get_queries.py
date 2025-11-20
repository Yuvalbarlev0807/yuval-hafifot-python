get_post_by_id_query = """
{
  post(id: 2) {
    id
    title
    body
  }
}
"""
get_user_by_id_query = """ 
query {
  user(id: 1) {
    id
    username
    email
    address {
      geo {
        lat
        lng
      }
    }
  }
}
"""