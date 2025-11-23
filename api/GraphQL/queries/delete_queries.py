delete_post_query = """
  mutation (
  $id: ID!
) {
  deletePost(id: $id)
}
"""
