// Generated by @typespec/http-server-csharp
// <auto-generated />
#nullable enable

      using System;using System.Text.Json;using System.Text.Json.Serialization;using TypeSpec.Helpers.JsonConverters;using System.Net;using System.Threading.Tasks;using Microsoft.AspNetCore.Mvc;using Microsoft.ContosoProviderHub.Service.Models;

      namespace Microsoft.ContosoProviderHub.Service {

      public interface IOperations {
      ///<summary>
/// List the operations for the provider
///</summary>
Task<OperationListResult> ListAsync( string apiVersion);

    }
   } 
