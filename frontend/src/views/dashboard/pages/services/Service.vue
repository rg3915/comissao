<template>
  <v-container
    id="user-profile"
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col
        cols="12"
        md="8"
      >
        <base-material-card>
          <template v-slot:heading>
            <div class="text-h3 font-weight-light">
              Editar Serviço
            </div>
          </template>

          <v-form @submit.prevent="submitForm">
            <v-container class="py-0">
              <v-row>
                <v-col
                  cols="12"
                  md="12"
                >
                  <v-text-field
                    v-model="item.description"
                    label="Descrição"
                    value="Sobrancelha"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    v-model="item.price"
                    class="purple-input"
                    label="Preço"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    v-model="item.comission"
                    label="Comissão"
                    class="purple-input"
                  />
                </v-col>

                <v-col
                  cols="12"
                  class="text-right"
                >
                  <v-btn
                    color="success"
                    class="mr-0"
                    type="submit"
                  >
                    Salvar
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </base-material-card>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        item: {},
      }
    },
    mounted () {
      this.getData()
    },
    methods: {
      getData () {
        const id = this.$route.params.id

        axios.get(`/api/v1/services/${id}`)
          .then(response => {
            this.item = response.data
          })
      },
      async submitForm () {
        const id = this.$route.params.id

        axios
          .patch(`/api/v1/services/${id}/`, this.item)
          .then(() => {
            this.$router.push({ name: 'Serviços' })
          })
          .catch(error => {
            console.log(error)
          })
      },
    },
  }
</script>
