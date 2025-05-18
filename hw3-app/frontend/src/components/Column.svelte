<script lang="js">
  import Article from "./Article.svelte";

  let { articles } = $props();
</script>

<section class="column">
  {#each articles as article, i}
    <Article articleInfo={article} id={i}/>
  {/each}
</section>
