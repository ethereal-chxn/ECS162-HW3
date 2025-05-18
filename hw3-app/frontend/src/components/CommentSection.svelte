<script lang="js">
  import CommentBox from "./CommentBox.svelte";
  import Comment from "./Comment.svelte";
  
  let {articleId, onClickHandler, comments} = $props();
  // console.log($state.snapshot(comments));
</script>

<section class="comment-section">
  <div class="comment-section-header">
    <button onclick={onClickHandler}>X</button>
  </div>

  <h2>Comments</h2>

  <CommentBox articleId={articleId}/>

  {#each comments as comment}
    <Comment 
      author={comment["author"]} 
      commentBody={comment["commentBody"]}
    /> 
  {/each}
</section>
