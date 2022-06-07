<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Fornecedores"
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
              <a href="#/pages/crm/provider">{{ item.name }}</a>
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
          Editar Fornecedor

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
                  value="Christina"
                />
              </v-col>

              <v-col
                cols="12"
                md="4"
              >
                <v-text-field
                  class="purple-input"
                  label="Sobrenome"
                  value="Powell"
                />
              </v-col>

              <v-col
                cols="12"
                md="4"
              >
                <v-text-field
                  class="purple-input"
                  label="Gênero"
                  value="Feminino"
                />
              </v-col>

              <v-col
                cols="12"
                md="6"
              >
                <v-text-field
                  class="purple-input"
                  label="E-mail"
                  value="christina@powell.com"
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
  export default {
    data () {
      return {
        items: [
          {
            name: 'Christina Powell',
            email: 'christina@powell.com',
            phone: '91964-9594',
          },
          {
            name: 'Colin Matthews',
            email: 'colin@matthews.com',
            phone: '96643-0486',
          },
          {
            name: 'Courtney Myers',
            email: 'courtney@myers.com',
            phone: '92424-2523',
          },
          {
            name: 'James Gibson',
            email: 'james@gibson.com',
            phone: '99781-2644',
          },
          {
            name: 'Lisa Ross',
            email: 'lisa@ros.coms',
            phone: '95155-6367',
          },
          {
            name: 'Megan Miles',
            email: 'megan@miles.com',
            phone: '99854-1449',
          },
          {
            name: 'Nicole Deleon',
            email: 'nicole@deleon.com',
            phone: '99984-3576',
          },
          {
            name: 'Paul Miller',
            email: 'paul@miller.com',
            phone: '94264-6400',
          },
          {
            name: 'Rebecca Butler',
            email: 'rebecca@butler.com',
            phone: '91806-5236',
          },
          {
            name: 'Rodney Rodriguez',
            email: 'rodney@rodriguez.com',
            phone: '98352-0529',
          },
        ],
        dialog: false,
      }
    },
  }
</script>
