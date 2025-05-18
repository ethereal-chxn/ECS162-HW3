<script lang="js">
  import CommentBox from "./CommentBox.svelte";
  
  let {articleId, onClickHandler} = $props();
</script>

<section class="comment-section">
  <div class="comment-section-header">
    <button onclick={onClickHandler}>X</button>
  </div>
  <h2>Comments</h2>
  <CommentBox articleId={articleId}/>
</section>
