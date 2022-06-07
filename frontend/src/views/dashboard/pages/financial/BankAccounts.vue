<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Bancos"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Nome do Banco
            </th>
            <th class="primary--text">
              Número do Banco
            </th>
            <th class="primary--text">
              Agência
            </th>
            <th class="primary--text">
              Conta
            </th>
            <th class="text-right primary--text">
              Editar
            </th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td>Banco do Brasil</td>
            <td>001</td>
            <td>0741-9</td>
            <td>724900-0</td>
            <td class="text-right">
              <v-icon class="mx-1">
                mdi-pencil
              </v-icon>
            </td>
          </tr>

          <tr>
            <td>Itaú</td>
            <td>341</td>
            <td>46840</td>
            <td>7246480-0</td>
            <td class="text-right">
              <v-icon class="mx-1">
                mdi-pencil
              </v-icon>
            </td>
          </tr>

          <tr>
            <td>Santander</td>
            <td>033</td>
            <td>67808</td>
            <td>97034570</td>
            <td class="text-right">
              <v-icon class="mx-1">
                mdi-pencil
              </v-icon>
            </td>
          </tr>

          <tr>
            <td>NuBank</td>
            <td>260</td>
            <td>768</td>
            <td>38706035</td>
            <td class="text-right">
              <v-icon class="mx-1">
                mdi-pencil
              </v-icon>
            </td>
          </tr>
        </tbody>
      </v-simple-table>
    </base-material-card>
  </v-container>
</template>
