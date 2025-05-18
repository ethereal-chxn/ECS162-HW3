<script lang="js">
  import Article from "./Article.svelte";

  let { articles, idList, clickHandler } = $props();
</script>

<section class="column">
  {#each articles as article, i}
    <Article articleInfo={article} id={idList[i]} clickHandler={clickHandler}/>
  {/each}
</section>
