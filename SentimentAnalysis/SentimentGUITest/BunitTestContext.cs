using Bunit;
using NUnit.Framework;

namespace SentimentGUITest;

/// <summary>
/// Test context wrapper for bUnit. BtB
/// Read more about using <see cref="BunitTestContext"/> <seealso href="https://bunit.dev/docs/getting-started/writing-tests.html#remove-boilerplate-code-from-tests">here</seealso>.
/// </summary>
public abstract class BunitTestContext : TestContextWrapper
{
	[SetUp]
	public void Setup() => TestContext = new Bunit.TestContext();

	[TearDown]
	public void TearDown() => TestContext?.Dispose();
}
