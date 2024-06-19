
<script setup lang="ts">

import {ref, reactive} from 'vue'
import axios from 'axios'

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

 const survivalProbability = ref<number|undefined>()

 const validateRequestValues = (): boolean => {
   if (features.Sex == 'What is your gender?') {
     alert('Fill in your gender')
     return false
   }
   if (features.Pclass == 'What is your class?') {
     alert('Fill in your class')
     return false
   } 
   if (features.Age == 'How old are you?') {
     alert('Fill in your age')
     return false
   } 
   if (features.Parch == 'How many parents and children are you with?') {
     alert('Fill in the number of children')
     return false
   } 
   if (features.SibSp == 'How many siblings are you with?') {
     alert('Fill in the number of siblings')
     return false
   }
   return true  
 }

//  const displayOutput = (): void => {
//    alert(`
//      Gender: ${features.Sex}
//      Class: ${features.Pclass} 
//      Age: ${features.Age} 
//      Parents: ${features.Parch} 
//      Siblings: ${features.SibSp}
//    `)
//   }


const displayOutput = (): void => {
   
   const endPoint: string = 'http://localhost:5001/api/titanic'
   const validationResult: boolean = validateRequestValues()
   if (validationResult === true) { 
     axios.post(
       endPoint, features
     ).then(
       (response) => {
         survivalProbability.value = 100 * response.data.survival_probability as number
       }
     ).catch(
       () => {
         alert('エラーが発生しました。')
       } 
     )
   }
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
   <template v-if="survivalProbability !== undefined">
     <div class="alert alert-error mt-4 ">
       Your survival rate is {{ survivalProbability }}
     </div>
   </template>
 </div>
</template>