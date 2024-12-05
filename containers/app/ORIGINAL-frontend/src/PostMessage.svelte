<script>
  let newTitle = "";
  let newDescription = "";

  async function addMessage() {
    try {
      const response = await fetch("/api/messages", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ title: newTitle, description: newDescription }),
      });

      if (response.ok) {
        alert("Message added successfully!");
        newTitle = "";
        newDescription = "";
      } else {
        alert("Failed to add message.");
      }
    } catch (error) {
      console.error("Error adding message:", error);
    }
  }
</script>

<div class="flex flex-col items-center justify-center min-h-screen bg-gray-100">
  <h1 class="text-2xl mb-4">Post a Message</h1>
  <input bind:value={newTitle} placeholder="Title" class="border p-2 m-2" />
  <input
    bind:value={newDescription}
    placeholder="Description"
    class="border p-2 m-2"
  />
  <button
    on:click={addMessage}
    class="bg-green-500 text-white px-4 py-2 rounded">Add Message</button
  >
</div>

<style>
  /* Add any additional styles here */
</style>