using Microsoft.EntityFrameworkCore;
using WebStore.Data;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddDbContext<MyStoreDbContext>(options =>
    options.UseNpgsql(builder.Configuration.GetConnectionString("MyConnectionString")));

builder.Services.AddControllers();

var app = builder.Build();

// Configure the HTTP request pipeline.

app.UseAuthorization();

app.MapControllers();

app.Run();
