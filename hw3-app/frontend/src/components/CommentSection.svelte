<script lang="js">
  import CommentBox from "./CommentBox.svelte";
  
  let articleId = $props();
</script>

<section class="comment-section">
  <h2>Comments</h2>
  <CommentBox articleId={articleId}/>
</section>
