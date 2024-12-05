<script>
  import { onMount, onDestroy } from "svelte";
  // import { ProxyAgent } from "undici";
  let entries = [];
  let currentEntryIndex = 0;
  let entryTimeout = null;
  let updateInterval = null;
  let pauseBetweenEntries = 4000;
  let loop = true;
  let displayContent = [];

  /* We use a fake RSS Feed for testing purposes
   * https://newsthump.com/feed/
   * replace by
   * http://web:5000/feed.xml
   */
  const RSS_FEED_URL = "https://newsthump.com/feed/"; // API URL for fetching messages
  const POLLING_INTERVAL = 600000; // 1 minute
  // const dispatcher = new ProxyAgent("http://myproxy.company.com:8080");

  async function fetchRSSFeed() {
    const response = await fetch(RSS_FEED_URL, {
      // dispatcher,
      mode: "no-cors",
      headers: {
        "Content-Type": "application/rss+xml",
      },
    });
    console.debug("response: ", response);
    if (response.ok) {
      console.debug("Response from RSS Feed received");
      const text = await response.text();
      const parser = new DOMParser();
      const xml = parser.parseFromString(text, "text/xml");
      const items = Array.from(xml.querySelectorAll("item"));
      console.debug("items: ", items);
      entries = items.map((item) => ({
        rows: 1,
        segments: 10,
        rowValues: [item.querySelector("title").textContent],
      }));
      console.debug("entries: ", entries);
      currentEntryIndex = 0; // Reset index
      loadFromJSON(entries[currentEntryIndex]);
    } else {
      // throw new Error(`unexpected network error: ${response.status}`);
      /* Temporarily mocking the feed */
      console.debug("Response from RSS Feed mocked");
      const text = `<?xml version="1.0" encoding="UTF-8" ?>
        <rss version="2.0">
            <channel>
                <title>Example RSS feed</title>
                <link>https://www.example.com/messages.xml</link>
                <description>This RSS feed is about messages</description>
                
                <item>
                    <title>My First Message</title>
                    <link>http://example.com/messages/first/</link>
                    <description>The description of my first message.</description>
                </item>
                
                <item>
                    <title>My Second Message</title>
                    <link>http://example.com/messages/second/</link>
                    <description>The description of my second message.</description>
                </item>

                <item>
                    <title>My Third Message</title>
                    <link>http://example.com/messages/third/</link>
                    <description>The description of my third message.</description>
                </item>

            </channel>
        </rss>`;
      const parser = new DOMParser();
      const xml = parser.parseFromString(text, "text/xml");
      const items = Array.from(xml.querySelectorAll("item"));
      console.debug("items: ", items);
      entries = items.map((item) => ({
        rows: 1,
        segments: 10,
        rowValues: [item.querySelector("title").textContent],
      }));
      console.debug("entries: ", entries);
      currentEntryIndex = 0; // Reset index
      loadFromJSON(entries[currentEntryIndex]);
    }
  }

  function processEntries() {
    console.debug("processEntries");
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
    console.debug("loadFromJSON");
    displayContent = entry.rowValues.map((value) => {
      return {
        value,
        segments: value.split("").map((char) => ({
          char,
          glyphs: [char], // Default to the character itself
        })),
      };
    });
    console.debug("displayContent: ", displayContent);
  }

  function startDisplay() {
    console.debug("startDisplay");
    processEntries();
  }

  function stopDisplay() {
    console.debug("stopDisplay");
    clearTimeout(entryTimeout);
  }

  onMount(async () => {
    console.debug("onMount");
    await fetchRSSFeed();
    startDisplay();
    updateInterval = setInterval(fetchRSSFeed, POLLING_INTERVAL);
  });

  onDestroy(() => {
    console.debug("onDestroy");
    clearInterval(updateInterval);
    stopDisplay();
  });
</script>

<div class="flex flex-col items-center justify-center min-h-screen bg-gray-100">
  <div class="splitflap">
    {#each displayContent as row}
      <div class="row">
        {#each row.segments as segment}<div class="segment">
            {segment.char}
          </div>{/each}
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
