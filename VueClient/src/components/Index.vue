<template>
    <BookTable :data="data" @book-id="UpdateEvent"/>
</template>

<script setup>

  //  Importing Components
  import BookTable from './Books.vue';


  //  Importing required dependencies
  import { reactive, watch } from 'vue';

  //  Initializing reactive objects
  const Book = reactive
  (
      {
        id    :null,
        title :null,
        author:null,
      }
  );

  const data = reactive(  
    {
      title: null,
      author: null,
  });

  function SubmitBook(payload)
  {
    console.log("Submitting :", payload);
    if (payload.id)
    {
        data.id = payload.id;
    }
    data.title = payload.title;
    data.author = payload.author;
  }
  function UpdateEvent(payload)
  {
      Book.id = payload;
  }

  watch(Book, (data) => {
    console.log("Data: ", data);
  },
  );
</script>