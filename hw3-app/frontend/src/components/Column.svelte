<script lang="ts">
  import Article from "./Article.svelte";

  let { articles } = $props();
</script>

<section class="column">
  {#each articles as article}
    <Article articleInfo={article} />
  {/each}
</section>
