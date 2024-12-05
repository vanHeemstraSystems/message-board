<script>
  import { onMount, onDestroy } from "svelte";

  let entries = [];
  let currentEntryIndex = 0;
  let entryTimeout = null;
  let updateInterval = null;
  let pauseBetweenEntries = 4000;
  let loop = true;
  let displayContent = [];

  const RSS_FEED_URL = "http://web:5000/feed.xml"; // API URL for fetching messages
  const POLLING_INTERVAL = 60000; // 1 minute

  async function fetchRSSFeed() {
    const response = await fetch(RSS_FEED_URL);
    if (response.ok) {
      const text = await response.text();
      const parser = new DOMParser();
      const xml = parser.parseFromString(text, "text/xml");
      const items = Array.from(xml.querySelectorAll("item"));

      entries = items.map((item) => ({
        rows: 1,
        segments: 10,
        rowValues: [item.querySelector("title").textContent],
      }));

      currentEntryIndex = 0; // Reset index
      loadFromJSON(entries[currentEntryIndex]);
    }
  }

  function processEntries() {
    if (currentEntryIndex >= entries.length) {
      if (loop) {
        currentEntryIndex = 0;
      } else {
        return;
      }
    }

    loadFromJSON(entries[currentEntryIndex]);
    currentEntryIndex++;

    entryTimeout = setTimeout(processEntries, pauseBetweenEntries);
  }

  function loadFromJSON(entry) {
    displayContent = entry.rowValues.map((value) => {
      return {
        value,
        segments: value.split("").map((char) => ({
          char,
          glyphs: [char], // Default to the character itself
        })),
      };
    });
  }

  function startDisplay() {
    processEntries();
  }

  function stopDisplay() {
    clearTimeout(entryTimeout);
  }

  onMount(async () => {
    await fetchRSSFeed();
    startDisplay();
    updateInterval = setInterval(fetchRSSFeed, POLLING_INTERVAL);
  });

  onDestroy(() => {
    clearInterval(updateInterval);
    stopDisplay();
  });
</script>

<div class="flex flex-col items-center justify-center min-h-screen bg-gray-100">
  <div class="splitflap">
    {#each displayContent as row}
      <div class="row">
        {#each row.segments as segment}
          <div class="segment">
            {segment.char}
          </div>
        {/each}
      </div>
    {/each}
  </div>
</div>

<style>
  .splitflap {
    @apply bg-white p-6 rounded-lg shadow-lg;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .row {
    @apply flex;
    height: 50px; /* Height of each row */
    overflow: hidden;
    position: relative;
  }

  .segment {
    @apply w-8 h-full bg-gray-200 text-center flex items-center justify-center font-mono text-lg;
    border: 1px solid #ccc;
  }
</style>
