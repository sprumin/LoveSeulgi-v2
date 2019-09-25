<template>
    <v-container>
        <v-layout row wrap>
            <v-flex xs6>
                <List/>
            </v-flex>
            <v-flex xs6>
                <ListAdd/>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import List from './List'
import ListAdd from './ListAdd'

export default {
    components: {
        List,
        ListAdd
    }
}
</script>