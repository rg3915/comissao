<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Funcionários"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Nome
            </th>
            <th class="primary--text">
              E-mail
            </th>
            <th class="primary--text">
              Telefone
            </th>
            <th class="text-right primary--text">
              Editar
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="item in items"
            :key="item"
          >
            <td>
              <a href="#/pages/crm/employee">{{ item.name }}</a>
            </td>
            <td>{{ item.email }}</td>
            <td>{{ item.phone }}</td>
            <td class="text-right">
              <v-icon
                class="mx-1"
                @click="dialog = true"
              >
                mdi-pencil
              </v-icon>
            </td>
          </tr>
        </tbody>
      </v-simple-table>
    </base-material-card>

    <v-dialog
      v-model="dialog"
      max-width="500"
    >
      <v-card class="text-center">
        <v-card-title>
          Editar Funcionário

          <v-spacer />

          <v-icon
            aria-label="Close"
            @click="dialog = false"
          >
            mdi-close
          </v-icon>
        </v-card-title>

        <v-form>
          <v-container class="py-0">
            <v-row>
              <v-col
                cols="12"
                md="4"
              >
                <v-text-field
                  label="Nome"
                  value="Alec"
                />
              </v-col>

              <v-col
                cols="12"
                md="4"
              >
                <v-text-field
                  class="purple-input"
                  label="Sobrenome"
                  value="Thompson"
                />
              </v-col>

              <v-col
                cols="12"
                md="4"
              >
                <v-text-field
                  class="purple-input"
                  label="Gênero"
                  value="Masculino"
                />
              </v-col>

              <v-col
                cols="12"
                md="6"
              >
                <v-text-field
                  class="purple-input"
                  label="E-mail"
                  value="alec@thompson.com"
                />
              </v-col>

              <v-col
                cols="12"
                md="6"
              >
                <v-text-field
                  label="Data de Nascimento"
                  class="purple-input"
                />
              </v-col>

              <v-col
                cols="12"
                md="6"
              >
                <v-text-field
                  label="CPF"
                  class="purple-input"
                />
              </v-col>

              <v-col
                cols="12"
                md="6"
              >
                <v-text-field
                  label="RG"
                  class="purple-input"
                />
              </v-col>

              <v-col cols="12">
                <v-text-field
                  label="Endereço"
                  class="purple-input"
                />
              </v-col>

              <v-col
                cols="12"
                md="4"
              >
                <v-text-field
                  label="Bairro"
                  class="purple-input"
                />
              </v-col>

              <v-col
                cols="12"
                md="4"
              >
                <v-text-field
                  label="Cidade"
                  class="purple-input"
                />
              </v-col>

              <v-col
                cols="12"
                md="4"
              >
                <v-text-field
                  class="purple-input"
                  label="CEP"
                  type="number"
                />
              </v-col>

              <v-col
                cols="12"
                class="text-right"
              >
                <v-btn
                  text
                  class="mr-5"
                  @click="dialog = false"
                >
                  Cancelar
                </v-btn>
                <v-btn
                  color="success"
                  class="mr-0"
                  @click="dialog = false"
                >
                  Salvar
                </v-btn>
              </v-col>
            </v-row>
          </v-container>
        </v-form>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        items: [
          {
            name: 'Alec Thompson',
            email: 'alec@thompson.com',
            phone: '97031-0000',
          },
          {
            name: 'Priscila Jones',
            email: 'priscila@jones.com',
            phone: '91310-0101',
          },
          {
            name: 'Sage Rodriguez',
            email: 'sage@rodriguez.com',
            phone: '94600-7600',
          },
          {
            name: 'Philip Chaney',
            email: 'philip@chaney.com',
            phone: '98730-0050',
          },
          {
            name: 'Doris Green',
            email: 'doris@green.com',
            phone: '95300-4503',
          },
        ],
        dialog: false,
      }
    },
    mounted () {
      this.getData()
    },
    methods: {
      getData () {
        axios.get('/api/v1/employees/')
          .then(response => {
            this.items = response.data
          })
      },
    },
  }
</script>
