<script setup lang="ts">
import {reactive} from 'vue'
 type typeOfFeatures = {
  Sex: 'Male'|'Female'|'What is your gender?'
  Pclass: string
  Age: number|'How old are you?'
  Parch: number|'How many parents and children are you with?'
  SibSp: number|'How many siblings are you with?'
 }


 const features = reactive<typeOfFeatures>({
   Sex: 'What is your gender?',
   Pclass: 'What is your class?',
   Age: 'How old are you?',
   Parch: 'How many parents and children are you with?',
   SibSp: 'How many siblings are you with?'
 })

 const displayOutput = (): void => {
   alert(`
     Gender: ${features.Sex}
     Class: ${features.Pclass} 
     Age: ${features.Age} 
     Parents: ${features.Parch} 
     Siblings: ${features.SibSp}
   `)
  }



</script>

<template>

<div class="container mx-auto mt-4">

  <select class="select select-primary mb-4" v-model="features.Sex">
   <option disabled selected>What is your gender?</option>
   <option>Male</option>
   <option>Female</option>
   </select>

   <br>

   <select class="select select-primary mb-4" v-model="features.Pclass">
     <option disabled selected>What is your class?</option>
     <option>Upper class</option>
     <option>Middle class</option>
     <option>Lower class</option>
   </select>
   
   <br> 

    <select class="select select-primary mb-4" v-model="features.Age">
     <option disabled selected>How old are you?</option>
     <option v-for="i in [...Array(121).keys()]">
      {{ i }}
      </option>
   </select> years old
   <br>
   
    <select class="select select-primary mb-4" v-model="features.Parch">
     <option disabled selected>How many parents and children are you with?</option>
     <option v-for="i in [...Array(11).keys()]">
       {{ i }} 
     </option>
   </select> people
   <br>

   <select class="select select-primary mb-4" v-model="features.SibSp">
     <option disabled selected>How many siblings are you with?</option>
     <option v-for="i in [...Array(11).keys()]">
       {{ i }} 
     </option>
   </select> people
   <br>
   <button class="btn btn-primary" v-on:click="displayOutput()">output the result</button>
 </div>
</template>