<template>
    <div>
        <v-textarea
            outline
            v-model="memo"
            label="Please Input Todo List"
            value=""
        ></v-textarea>
        <v-btn @click="listAdd">AddList</v-btn>
    </div>
</template>

<script>
export default {
    data() {
        return {
            memo: null
        }
    },
    methods: {
        listAdd() {
            console.log("List Add!")
            if(this.memo === null){
                alert("Invalid memo")
            } else {
                this.$emit("listAdd", this.memo)
            }
        }
    }
}
</script>